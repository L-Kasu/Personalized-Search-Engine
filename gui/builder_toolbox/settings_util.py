import json
from gui.builder_toolbox.settings_defaultpaths import *
from restart_application import restart_application


def write_config(config, path=default_path, file=masterconfigfile):
    with open(path + file, 'w') as configfile:
        json.dump(config, configfile, indent=4)
        configfile.close()


def edit_config(config_dict, path=default_path, file=masterconfigfile):
    with open(path + file, 'r') as configfile:
        config = json.load(configfile)
        for key in config_dict:
            config[key] = config_dict[key]
        configfile.close()
    with open(path + file, 'w') as configfile:
        json.dump(config, configfile, indent=4)
        configfile.close()


def get_config(key, path=default_path, file=masterconfigfile):
    with open(path + file, 'r') as configfile:
        config = json.load(configfile)
        value = config[key]
    return value


def get_configdict(path=default_path, file=masterconfigfile):
    with open(path + file, 'r') as configfile:
        config = json.load(configfile)
        configfile.close()
    return config


def set_language(self,
                 lang,
                 path=default_path,
                 file=languageconfigfile,
                 masterfile=masterconfigfile):
    configdict = get_configdict(path, file)
    config = {}
    for key in configdict:
        if key == lang:
            config = configdict[key]
    edit_config(config, path, masterfile)
    restart_application(self)


def set_colors(self,
               template,
               path=default_path,
               file=colorsconfigfile,
               masterfile=masterconfigfile):
    configdict = get_configdict(path, file)
    config = {}
    for key in configdict:
        if key == template:
            config = configdict[key]
    edit_config(config, path, masterfile)
    restart_application(self)
