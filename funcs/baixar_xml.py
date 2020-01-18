import pyodbc, os, untangle, shutil

def exe(conf_geral, dic):

    arquivo = open('sql/xml_chaves.sql', 'r')
    texto = arquivo.read()

    if 'back_day' in list(conf_geral):

        consulta = texto.replace(
            'CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,-1,GETDATE()),11) and',
            'CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,{},GETDATE()),11) and'
                .format(conf_geral['back_day'])
        )

    elif 'date' in list(conf_geral):

        consulta = texto.replace(
            'CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,-1,GETDATE()),11) and',
            "CONVERT(varchar(8),MDF.Data_Emissao, 11) = '{}' and"
                .format(conf_geral['date'])
        )

    else:

        consulta = texto

    conexao = \
        'DRIVER={ODBC Driver 17 for SQL Server};' \
        'SERVER=' + dic['ip'] + ',' + dic['porta'] + ';' \
        'DATABASE=S9_Real;' \
        'UID='+dic['usuario']+';' \
        'PWD='+dic['senha']

    cnxn = pyodbc.connect(conexao)
    cursor = cnxn.cursor()
    cursor.execute(consulta)
    table = cursor.fetchall()
    cnxn.close()

    if os.path.isdir(os.path.join(conf_geral['base_dir'],'xmls')) == True:
        shutil.rmtree(os.path.join(conf_geral['base_dir'],'xmls'))
    os.mkdir(os.path.join(conf_geral['base_dir'],'xmls'))

    if len(table) > 0:

        for row in table:

            xml = conf_geral['base_dir'] + 'xmls' + os.sep + row.CHAVE + '.xml'
            conteudo = row.XML_Documento
            xml_aut = row.XML_Autorizacao

            obj = untangle.parse(xml_aut)
            xmlns = obj.protNFe['xmlns']
            versao = obj.protNFe['versao']

            xml_ant = '<nfeProc xmlns="'+xmlns +'" versao="'+ versao +'">'
            xml_dep = '</nfeProc>'

            arquivo = open(xml,'w')
            arquivo.writelines(xml_ant + conteudo + xml_dep)
            arquivo.close()

        print(dic['empresa'] + ' - ' + str(len(table)) + ' arquivos xml gerados...')

        return 'yes'

    else:

        return 'no'