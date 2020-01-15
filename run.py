import os
from funcs import baixar_xml, compactar, email

base_dir = os.path.expanduser('~') + os.sep + 'Desktop' + os.sep

confs = {
    'Novo Aviamento':{
        'ip':'186.235.189.90',
        'porta':'1439',
        'usuario':'sa',
        'senha':'Senha123',
        'titulo':'Novo Aviamento - XML',
        'end_email':'diogo_k0@hotmail.com'
    }
}

for conf in confs:

    print('Baixando arquivo...')
    baixar_xml.exe(base_dir, confs[conf])
    print('Compactanto arquivos...')
    compactar.exe(base_dir)
    print('Enviando email...')
    email.exe(base_dir, confs[conf])
    print('Processo concluido...')