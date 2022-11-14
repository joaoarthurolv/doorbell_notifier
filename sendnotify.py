#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os

USERNAME = "youremail@gmail.com"
PASSWORD = "yourpassword"

#def sendMail(to, subject, text, files=[] -- When you want to attach files to the email
def sendMail(to, subject, text):
    assert type(to)==list
#    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

#    for file in files:
#        part = MIMEBase('application', "octet-stream")
#        part.set_payload( open(file,"rb").read() )
#        Encoders.encode_base64(part)
#        part.add_header('Content-Disposition', 'attachment; filename="%s"'
#                       % os.path.basename(file))
#        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME, to, msg.as_string())
    server.quit()

sendMail( ["youremail@gmail.com"],
        "Notificacao de Campanhia",
        "Alguem esta tocando a campanhia")
#        ["/home/pi/webcam.jpg"] )
