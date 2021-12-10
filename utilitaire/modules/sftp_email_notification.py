import re
import os
import ntpath
import sys
import time
import json
from tqdm import tqdm
from glob import glob

# Modules à installer avant la publication
import ftplib
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, ProgressBar, ReverseBar, RotatingMarker, SimpleProgress, Timer, UnknownLength

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Vérifie si le fichier est présent
def check_sftp(sftp_host, username, password, path, file):
    return

# Envoie un email
def send_email(smtp_exp, smtp_dest, smtp_subject, smtp_message, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = smtp_exp
    msg['To'] = smtp_dest
    msg['Subject'] = smtp_subject
    message = smtp_message
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP(smtp_server, smtp_port)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(smtp_exp, smtp_password)
    mailserver.sendmail(smtp_exp, smtp_dest, msg.as_string())
    mailserver.quit()
    return

#SSL requis : oui
#Authentification requise : oui
#Port pour SSL : 465
#Port pour TLS/STARTTLS : 587
