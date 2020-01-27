import os, zipfile

def exe(paramentros, dic, list):

    for cnpj in list:

        nome_arq = dic[str(cnpj)] + ' - ' + str(cnpj) + '.zip'
        pasta_zip = str(os.path.join(paramentros['base_dir'][0],'zip'))

        fantasy_zip = zipfile.ZipFile(os.path.join(pasta_zip, nome_arq), 'w')

        pasta_xml = str(os.path.join(paramentros['base_dir'][0],'xmls' + os.sep + str(cnpj)))

        for folder, subfolders, files in os.walk(pasta_xml):
            for file in files:
                if file.endswith('.xml'):
                    fantasy_zip.write(os.path.join(folder, file), file, compress_type=zipfile.ZIP_DEFLATED)
        fantasy_zip.close()