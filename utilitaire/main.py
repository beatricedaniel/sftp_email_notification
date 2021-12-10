from modules import route_sftp,route_smtp ,sftp_email_notification

param_config_sftp = route_sftp.read_config_sftp_lecture("config/config.json")
sftp_username = param_config_sftp["username"]
sftp_password = param_config_sftp["password"]
sftp_host = param_config_sftp["sftp_host"]
print(sftp_username)
print(sftp_password)
print(sftp_host)

param_config_smtp = route_smtp.read_config_smtp("config/config.json")
smtp_username = param_config_smtp["username"]
smtp_password = param_config_smtp["password"]
smtp_server = param_config_smtp["server"]
smtp_port = param_config_smtp["port"]
smtp_exp = param_config_smtp["from"]
smtp_dest = param_config_smtp["to"]
smtp_subject = param_config_smtp["subject"]
smtp_message = param_config_smtp["message"]
print(smtp_username)
print(smtp_password)
print(smtp_server)
print(smtp_port)
print(smtp_exp)
print(smtp_dest)
#exe_check_sftp = sftp_email_notification.check_sftp()
exe_send_email = sftp_email_notification.send_email(
    smtp_exp=param_config_smtp["from"], 
    smtp_dest=param_config_smtp["to"], 
    smtp_subject=param_config_smtp["subject"], 
    smtp_message=param_config_smtp["message"], 
    smtp_server=param_config_smtp["server"], 
    smtp_port=param_config_smtp["port"], 
    smtp_username=param_config_smtp["username"], 
    smtp_password=param_config_smtp["password"])