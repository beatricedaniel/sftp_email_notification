import json

# Lecture de la configuration du serveur SFTP avec le compte en lecture
def read_config_smtp(path_in):
    print("--- Lancement de la lecture de la configuration du serveur smtp")
    with open(path_in) as f:
        dict_ret = json.load(f)
    L_ret = dict_ret["smtp"]
    param_config = {}
    for param in L_ret:
        param_config = param.copy()
    print("- Lecture de la configuration " + path_in + ".")
    return param_config