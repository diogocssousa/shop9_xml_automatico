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


def exe(base_dir, dic):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    acc_addr = 'diogocssousa.ds@gmail.com'
    acc_pwd = 'dcssousa1'

    to_addr = dic['end_email']

    body = ''

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(acc_addr, acc_pwd)

    msg = MIMEMultipart()
    msg["From"] = acc_addr
    msg["To"] = to_addr
    msg["Subject"] = dic['titulo']

    msgText = MIMEText('<b>{}</b>'.format(body),'html')
    msg.attach(msgText)

    adiciona_anexo(msg, os.path.join(base_dir,'xmls.zip'))

    server.sendmail(acc_addr, to_addr, msg.as_string())
    server.quit()