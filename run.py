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
