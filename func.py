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

    cnxn = pyodbc.connect(conexao)
    cursor = cnxn.cursor()
    cursor.execute(texto)
    table = cursor.fetchall()
    cnxn.close()

    if os.path.isdir(os.path.expanduser('~') + os.sep + 'Desktop' + os.sep + 'xmls') == True:
        shutil.rmtree(os.path.expanduser('~') + os.sep + 'Desktop' + os.sep + 'xmls')
    os.mkdir(os.path.expanduser('~') + os.sep + 'Desktop' + os.sep + 'xmls')

    for row in table:

        arquivo = open(row.CHAVE + '.txt', 'w')
        arquivo.close()

    print(len(table))