import pyodbc

arquivo = open('xml_chave', 'r')
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

    for row in table:
        print(row.CHAVE)

    print(len(table))