import os, shutil

def criar_pasta_xml(parametros):

    if os.path.isdir(os.path.join(parametros['base_dir'][0], 'xmls')) == True:
        shutil.rmtree(os.path.join(parametros['base_dir'][0], 'xmls'))
    os.mkdir(os.path.join(parametros['base_dir'][0], 'xmls'))

def criar_pasta_zip(parametros):

    if os.path.isdir(os.path.join(parametros['base_dir'][0], 'zip')) == True:
        shutil.rmtree(os.path.join(parametros['base_dir'][0], 'zip'))
    os.mkdir(os.path.join(parametros['base_dir'][0], 'zip'))

def criar_pasta_cnpj(parametros, cnpj):

    os.mkdir(os.path.join(parametros['base_dir'][0], 'xmls' + os.sep + str(cnpj)))

    return os.path.join(parametros['base_dir'][0], 'xmls' + os.sep + str(cnpj))