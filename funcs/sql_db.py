import pyodbc

def conexao(dic):

    conexao = \
        'DRIVER={ODBC Driver 17 for SQL Server};' \
        'SERVER=' + dic['ip'] + ',' + dic['porta'] + ';' \
        'DATABASE=S9_Real;' \
        'UID=' + dic['usuario'] + ';' \
        'PWD=' + dic['senha']

    return conexao


def select(conexao, consulta):

    cnxn = pyodbc.connect(conexao)
    cursor = cnxn.cursor()
    cursor.execute(consulta)
    table = cursor.fetchall()
    cnxn.close()

    return table


def filtro_01(parametros, sql_select):

    if 'data_inteiro' in list(parametros):

        consulta = sql_select.replace(
            'CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,-1,GETDATE()),11) and',
            'CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,{},GETDATE()),11) and'
                .format(parametros['data_inteiro'][0])
        )

    elif 'data' in list(parametros):

        consulta = sql_select.replace(
            'CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,-1,GETDATE()),11) and',
            "CONVERT(varchar(8),MDF.Data_Emissao, 11) = '{}' and"
                .format(parametros['data'][0])
        )

    elif 'periodo' in list(parametros):

        consulta = sql_select.replace(
            'CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,-1,GETDATE()),11) and',
            "CONVERT(varchar(8),MDF.Data_Emissao, 11) between '{}' and '{}'"
                .format(parametros['periodo'][0], parametros['periodo'][1])
        )

    else:

        consulta = sql_select

    return consulta


def filtro_02(cnpj, sql_select):

    if True:
        consulta = sql_select.replace(
            "F.CNPJ = '' and",
            "F.CNPJ = '{}' and"
                .format(str(cnpj))
        )

    return consulta