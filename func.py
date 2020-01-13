import pyodbc, os, shutil

arquivo = open('xml_chaves.txt', 'r')
texto = arquivo.read()

conexao = \
    'DRIVER={ODBC Driver 17 for SQL Server};' \
    'SERVER=186.235.189.90,1439;' \
    'DATABASE=S9_Real;' \
    'UID=sa;' \
    'PWD=Senha123'

def banco_de_dados():

    print('Iniciando processo...')

    cnxn = pyodbc.connect(conexao)

    print('Conexão ativa.')

    cursor = cnxn.cursor()
    cursor.execute(texto)

    print('Iniciando o carregamento dos arquivos.')

    table = cursor.fetchall()
    cnxn.close()

    print('XMLs coletados.')

    if os.path.isdir(os.path.expanduser('~') + os.sep + 'Desktop' + os.sep + 'xmls') == True:
        shutil.rmtree(os.path.expanduser('~') + os.sep + 'Desktop' + os.sep + 'xmls')
    os.mkdir(os.path.expanduser('~') + os.sep + 'Desktop' + os.sep + 'xmls')

    print('Escrevendo arquivos.')

    for row in table:

        xml = os.path.expanduser('~') + os.sep + 'Desktop' + os.sep + 'xmls' + os.sep + row.CHAVE + '.xml'
        conteudo = row.XML_Documento

        arquivo = open(xml,'w')
        arquivo.writelines(conteudo)
        arquivo.close()

    print(str(len(table)) + ' arquivos gerados.')