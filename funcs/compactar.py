import os, zipfile


def exe(conf_geral):

    caminho_inicial = os.getcwd()
    os.chdir(conf_geral['base_dir'])

    fantasy_zip = zipfile.ZipFile(os.path.join(conf_geral['base_dir'], 'xmls.zip'), 'w')

    for folder, subfolders, files in os.walk(os.path.join(conf_geral['base_dir'],'xmls')):
        for file in files:
            if file.endswith('.xml'):
                fantasy_zip.write(os.path.join(folder, file), file, compress_type=zipfile.ZIP_DEFLATED)
    fantasy_zip.close()

    os.chdir(caminho_inicial)