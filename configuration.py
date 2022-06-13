import configparser

def get_conf(header, row):
    try:
        config = configparser.ConfigParser()
        config.read('C:\\Service\\KainexusImport\\config.ini')
        result = config[header][row]
    except Exception as e:
        result = "error"
        print("[ERROR] Something wrong with configuration file: " + str(e))

    return result