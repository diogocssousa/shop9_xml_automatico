import os

def cnx():

    cnx = {
        'Novo Aviamento':{
            'habilitado':'yes',
            'empresa': 'Novo Aviamento',
            'ip':'186.235.189.90',
            'porta':'1439',
            'usuario':'sa',
            'senha':'Senha123',
            'titulo':'Novo Aviamento - XML',
        },
        'RJ Chaefer': {
            'habilitado': 'no',
            'empresa': 'RJ Chaefer',
            'ip': '45.4.147.69',
            'porta': '1410',
            'usuario': 'sa',
            'senha': 'Senha123',
            'titulo': 'R&J Chaefer - XML',
        },
        'Metropolis Atacado': {
            'habilitado': 'no',
            'empresa':'Metropolis Atacado',
            'ip': '186.235.191.141',
            'porta': '1434',
            'usuario': 'sa',
            'senha': 'Senha123',
            'titulo': 'Metropolis Moda Urbana - XML',
        },
        'Metropolis Varejo': {
            'habilitado': 'no',
            'empresa':'Metropolis Varejo',
            'ip': '186.235.191.141',
            'porta': '1314',
            'usuario': 'sa',
            'senha': 'Senha123',
            'titulo': 'Metropolis Moda Urbana - XML',
        },
    }

    return cnx

def param_default():

    # 'to_address' : 'diogo_k0@hotmail.com',
    # 'to_address' : 'depfiscal@contabli.com.br',
    # 'to_address' : 'nf-e_contabli@dominioboxe.com.br',
    # 'to_address' : 'contabli@cofresieg.com.br',
    # 'to_address' : 'nf-e_contabli@dominioboxe.com.br',

    param = {
        'base_dir': [os.getcwd()],
        'to_address':['contabli@cofresieg.com.br'],
        'smtp_server':['smtp.gmail.com'],
        'smtp_port':['587'],
        'acc_addr':['diogocssousa.ds@gmail.com'],
        'acc_pwd':['dcssousa1'],
    }

    return param