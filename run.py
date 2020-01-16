import os
from funcs import baixar_xml, compactar, email

base_dir = os.path.expanduser('~') + os.sep + 'Desktop' + os.sep

email_geral = 'diogo_k0@hotmail.com'
#email_geral = 'depfiscal@contabli.com.br'
#email_geral = 'nf-e_contabli@dominioboxe.com.br'

confs = {
    'Novo Aviamento':{
        'habilidado':'no',
        'empresa': 'Novo Aviamento',
        'ip':'186.235.189.90',
        'porta':'1439',
        'usuario':'sa',
        'senha':'Senha123',
        'titulo':'Novo Aviamento - XML',
        'end_email':email_geral
    },
    'RJ Chaefer': {
        'habilidado': 'no',
        'empresa': 'RJ Chaefer',
        'ip': '45.4.147.69',
        'porta': '1410',
        'usuario': 'sa',
        'senha': 'Senha123',
        'titulo': 'R&J Chaefer - XML',
        'end_email': email_geral
    },
    'Metropolis Atacado': {
        'habilidado': 'no',
        'empresa':'Metropolis Atacado',
        'ip': '186.235.191.141',
        'porta': '1434',
        'usuario': 'sa',
        'senha': 'Senha123',
        'titulo': 'Metropolis Moda Urbana - XML',
        'end_email': email_geral
    },
    'Metropolis Varejo': {
        'habilidado': 'no',
        'empresa':'Metropolis Varejo',
        'ip': '186.235.191.141',
        'porta': '1314',
        'usuario': 'sa',
        'senha': 'Senha123',
        'titulo': 'Metropolis Moda Urbana - XML',
        'end_email': email_geral
    },
}


for conf in confs:

    if confs[conf['habilitado']] == 'yes':

        print('{}'.format('-' * 50))
        print(conf + ' - Baixando arquivos...')
        continuar = baixar_xml.exe(base_dir, confs[conf])

        if continuar == 'yes':
            print(conf + ' - Compactanto arquivos...')
            compactar.exe(base_dir)

        if continuar == 'yes':
            print(conf + ' - Enviando email...')
            email.exe(base_dir, confs[conf])
            print(conf + ' - Processo concluido...')
            print('{}'.format('-' * 50))

        else:
            print(conf + ' - Nenhuma nota emitida...')
            print('{}'.format('-' * 50))
