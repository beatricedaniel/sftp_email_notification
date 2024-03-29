from modules import route_sftp,route_smtp ,sftp_email_notification


def check_file_sftp(config):
    param_config_sftp = route_sftp.read_config_sftp_lecture(config)
    sftp_username = param_config_sftp["username"]
    sftp_password = param_config_sftp["password"]
    sftp_host = param_config_sftp["sftp_host"]
    name = "-doctolib-rdv.csv"
    sftp_filename = sftp_email_notification.get_filename(name)
    sftp_path = "doctolib/"
    exe_check_if_true = sftp_email_notification.check_sftp(
        sftp_host, 
        sftp_username, 
        sftp_password, 
        sftp_path, 
        sftp_filename)
    return exe_check_if_true

response_of_check_if_true = check_file_sftp(config="config/config.json")

param_config_smtp = route_smtp.read_config_smtp("config/config.json")
smtp_username = param_config_smtp["username"]
smtp_password = param_config_smtp["password"]
smtp_server = param_config_smtp["server"]
smtp_port = param_config_smtp["port"]
smtp_exp = param_config_smtp["from"]
smtp_dest = param_config_smtp["to"]
smtp_subject = param_config_smtp["subject"]
smtp_message = param_config_smtp["message"]

if response_of_check_if_true == True:
    exe_send_email = sftp_email_notification.send_email(
        smtp_exp=param_config_smtp["from"], 
        smtp_dest=param_config_smtp["to"], 
        smtp_subject=param_config_smtp["subject"], 
        smtp_message=param_config_smtp["message"], 
        smtp_server=param_config_smtp["server"], 
        smtp_port=param_config_smtp["port"], 
        smtp_username=param_config_smtp["username"], 
        smtp_password=param_config_smtp["password"])
else:
    print("- ATTENTION le fichier Doctolib d'hier n'est pas encore disponible")
