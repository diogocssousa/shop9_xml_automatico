from funcs import conf, sql_db, dir
import sys, untangle, os

print('Iniciado...')
parametros = conf.param_default()

for param in sys.argv :

    try:
        var = str(param)
        p0 = var.split('=')[0]
        p1 = var.split('=')[1]
        lst = []

        try:
            var2 = str(p1)
            for i in range(0,len(var2.split('-'))):
                lst.append(var2.split('^')[i])
            parametros[p0] = lst

        except:
            parametros[p0] = [p1]

    except:
        continue

clientes = conf.cnx()

xml_cnpj = {}

dir.criar_pasta_xml(parametros)

for cliente in clientes:

    if clientes[cliente]['habilitado'] == 'yes':

        cnx_sql = sql_db.conexao(clientes[cliente])

        arq_sql_cnpjs = open('sql/xml_cnpjs.sql', 'r')
        sql_cnpj = arq_sql_cnpjs.read()
        cnpjs = sql_db.select(cnx_sql,sql_cnpj)
        lista_cnpj = []

        for cnpj in cnpjs:

            xml_cnpj[cnpj.CNPJ] = {}

        for cnpj in xml_cnpj:

            arq_sql_chaves = open('sql/xml_chaves.sql', 'r')
            sql_xml = arq_sql_chaves.read()

            filtro_01 = sql_db.filtro_01(parametros,sql_xml)
            filtro_02 = sql_db.filtro_02(cnpj, filtro_01)

            xmls = sql_db.select(cnx_sql, filtro_02)

            if len(xmls) > 0:

                pasta = dir.criar_pasta_cnpj(parametros, cnpj)

                print(str(cliente)+ ' - ' + str(cnpj) + ' - ' + str(len(xmls)))

                for row in xmls:
                    xml = pasta + os.sep + row.CHAVE + '.xml'
                    conteudo = row.XML_Documento
                    xml_aut = row.XML_Autorizacao

                    obj = untangle.parse(xml_aut)
                    xmlns = obj.protNFe['xmlns']
                    versao = obj.protNFe['versao']

                    xml_ant = '<nfeProc xmlns="' + xmlns + '" versao="' + versao + '">'
                    xml_dep = '</nfeProc>'

                    arquivo = open(xml, 'w')
                    arquivo.writelines(xml_ant + conteudo + xml_dep)
                    arquivo.close()
print('Concluido...')