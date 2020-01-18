import os, sys
from funcs import baixar_xml, compactar, email

# to_address = 'diogo_k0@hotmail.com'
# to_address = 'depfiscal@contabli.com.br'
# to_address = 'nf-e_contabli@dominioboxe.com.br'

parametros = {}
parametros['base_dir'] = os.path.expanduser('~') + os.sep + 'Desktop' + os.sep
parametros['to_address'] = 'nf-e_contabli@dominioboxe.com.br'

for param in sys.argv :

    try:
        var = str(param)
        p0 = var.split('=')[0]
        p1 = var.split('=')[1]
        parametros[p0] = p1

    except:
        continue


confs = {
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


for conf in confs:

    if confs[conf]['habilitado'] == 'yes':

        print('{}'.format('-' * 50))
        print(conf + ' - Baixando arquivos...')
        continuar = baixar_xml.exe(parametros, confs[conf])

        if continuar == 'yes':
            print(conf + ' - Compactanto arquivos...')
            compactar.exe(parametros)

        if continuar == 'yes':
            print(conf + ' - Enviando email...')
            email.exe(parametros, confs[conf])
            print(conf + ' - Processo concluido...')
            print('{}'.format('-' * 50))

        else:
            print(conf + ' - Nenhuma nota emitida...')
            print('{}'.format('-' * 50))
