import pyodbc, os, shutil, zipfile, smtplib, mimetypes, untangle

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

base_dir = os.path.expanduser('~') + os.sep + 'Desktop' + os.sep


def adiciona_anexo(msg, filename):
    if not os.path.isfile(filename):
        return

    ctype, encoding = mimetypes.guess_type(filename)

    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'

    maintype, subtype = ctype.split('/', 1)

    if maintype == 'text':
        with open(filename) as f:
            mime = MIMEText(f.read(), _subtype=subtype)

    else:
        with open(filename, 'rb') as f:
            mime = MIMEBase(maintype, subtype)
            mime.set_payload(f.read())

        encoders.encode_base64(mime)

    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(mime)


def banco_de_dados():

    arquivo = open('sql/xml_chaves.txt', 'r')
    texto = arquivo.read()

    conexao = \
        'DRIVER={ODBC Driver 17 for SQL Server};' \
        'SERVER=186.235.189.90,1439;' \
        'DATABASE=S9_Real;' \
        'UID=sa;' \
        'PWD=Senha123'

    print('Iniciando processo...')

    cnxn = pyodbc.connect(conexao)

    print('Conexão ativa...')

    cursor = cnxn.cursor()
    cursor.execute(texto)

    print('Iniciando o carregamento dos arquivos...')

    table = cursor.fetchall()
    cnxn.close()

    print('XMLs coletados...')

    if os.path.isdir(os.path.join(base_dir,'xmls')) == True:
        shutil.rmtree(os.path.join(base_dir,'xmls'))
    os.mkdir(os.path.join(base_dir,'xmls'))

    print('Escrevendo arquivos xmls...')

    for row in table:

        xml = base_dir + 'xmls' + os.sep + row.CHAVE + '.xml'
        conteudo = row.XML_Documento
        xml_aut = row.XML_Autorizacao

        obj = untangle.parse(xml_aut)
        xmlns = obj.protNFe['xmlns']
        versao = obj.protNFe['versao']

        xml_ant = '<nfeProc xmlns="'+xmlns +'" versao="'+ versao +'">'
        xml_dep = '</nfeProc>'

        arquivo = open(xml,'w')
        arquivo.writelines(xml_ant + conteudo + xml_dep)
        arquivo.close()

    print(str(len(table)) + ' arquivos xml gerados...')


def comprimir():

    print('Compactando...')

    caminho_inicial = os.getcwd()
    os.chdir(base_dir)

    fantasy_zip = zipfile.ZipFile(os.path.join(base_dir, 'xmls.zip'), 'w')

    for folder, subfolders, files in os.walk(os.path.join(base_dir,'xmls')):
        for file in files:
            if file.endswith('.xml'):
                fantasy_zip.write(os.path.join(folder, file), file, compress_type=zipfile.ZIP_DEFLATED)
    fantasy_zip.close()

    os.chdir(caminho_inicial)

    print('Arquivo compactado...')

def enviar_email():

    print('Enviando email...')

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    acc_addr = 'diogocssousa.ds@gmail.com'
    acc_pwd = 'dcssousa1'

    to_addr = 'diogo_k0@hotmail.com'

    subject = 'Arquivos xmls'
    body = ''

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(acc_addr, acc_pwd)

    msg = MIMEMultipart()
    msg["From"] = acc_addr
    msg["To"] = to_addr
    msg["Subject"] = subject

    msgText = MIMEText('<b>{}</b>'.format(body), 'html')
    msg.attach(msgText)

    adiciona_anexo(msg, os.path.join(base_dir,'xmls.zip'))

    server.sendmail(acc_addr, to_addr, msg.as_string())
    server.quit()

    print('Email enviado...')