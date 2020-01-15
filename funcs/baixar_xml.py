import pyodbc, os, untangle, shutil

def exe(base_dir, dic):

    arquivo = open('sql/xml_chaves.txt', 'r')
    texto = arquivo.read()

    conexao = \
        'DRIVER={ODBC Driver 17 for SQL Server};' \
        'SERVER=' + dic['ip'] + ',' + dic['porta'] + ';' \
        'DATABASE=S9_Real;' \
        'UID='+dic['usuario']+';' \
        'PWD='+dic['senha']

    cnxn = pyodbc.connect(conexao)
    cursor = cnxn.cursor()
    cursor.execute(texto)
    table = cursor.fetchall()
    cnxn.close()

    if os.path.isdir(os.path.join(base_dir,'xmls')) == True:
        shutil.rmtree(os.path.join(base_dir,'xmls'))
    os.mkdir(os.path.join(base_dir,'xmls'))

    for row in table:

        xml = base_dir + 'xmls' + os.sep + row.CHAVE + '.xml'
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

    print(str(len(table)) + ' arquivos xml gerados...')