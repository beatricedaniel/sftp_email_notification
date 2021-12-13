import json

# Lecture de la configuration du serveur SFTP avec le compte en lecture
def read_config_sftp_lecture(path_in):
    print("--- Lancement de la lecture de la configuration du serveur SFTP en lecture")
    with open(path_in) as f:
        dict_ret = json.load(f)
    L_ret = dict_ret["sftp_lecture"]
    param_config = {}
    for param in L_ret:
        param_config = param.copy()
    print("- Lecture de la configuration " + path_in + ".")
    return param_config
