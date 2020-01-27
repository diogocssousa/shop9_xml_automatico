import os, smtplib, mimetypes

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


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


def enviar(conf_geral, dic, cnpj):

    smtp_server = conf_geral['smtp_server'][0]
    smtp_port = conf_geral['smtp_port'][0]

    acc_addr = conf_geral['acc_addr'][0]
    acc_pwd = conf_geral['acc_pwd'][0]

    to_addr = conf_geral['to_address'][0]

    body = ''

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(acc_addr, acc_pwd)

    msg = MIMEMultipart()
    msg["From"] = acc_addr
    msg["To"] = to_addr
    msg["Subject"] = dic['titulo'] + ' - ' + str(cnpj)

    msgText = MIMEText('<b>{}</b>'.format(body),'html')
    msg.attach(msgText)

    nome_arq = dic['empresa'] + ' - ' + str(cnpj) + '.zip'
    pasta_xml = str(os.path.join(conf_geral['base_dir'][0], 'zip'))

    adiciona_anexo(msg, os.path.join(pasta_xml, nome_arq))

    server.sendmail(acc_addr, to_addr, msg.as_string())
    server.quit()