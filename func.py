import pyodbc

def banco_de_dados():

    cnxn = pyodbc.connect(conexao)
    cursor = cnxn.cursor()
    cursor.execute(select_01(i))
    nome = 'db_' + i
    db = cursor.fetchall()
    dic[nome] = db