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

import datetime

# Obtenir le nom du fichier doctolib de la veille déposé aujourd'hui
def get_filename(name):
    sftp_filename = (str(datetime.date.today()-datetime.timedelta(1))+name)
    return sftp_filename

# Vérifie si le fichier est présent
def check_sftp(sftp_host, sftp_username, sftp_password, sftp_path, sftp_filename):
    print("--- Lancement de la vérification de la dispo du fichier Doctolib de la veille")
    host = sftp_host
    username = sftp_username
    password = sftp_password
    sftp = ftplib.FTP(host, username, password)
    path = sftp_path+sftp_filename
    list_sftp = sftp.nlst(sftp_path)
    if path in list_sftp:
        return True
    else:
        return False

# Envoie un email
def send_email(smtp_exp, smtp_dest, smtp_subject, smtp_message, smtp_server, smtp_port, smtp_username, smtp_password):
    print("- Envoi de la notification par email.")
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
