# This file is used to initialise important things on startup.

# This includes reading the Dolphin directory, the Dolphin user directory, the game
# covers directory and user settings. It will handle accordingly if these are not found.

import configparser, os, subprocess

app_config = configparser.ConfigParser()
dolphin_config = configparser.ConfigParser()

def init():
    print(r'User AppData\Roaming directory: ' + os.getenv('APPDATA'))
    app_config.read("cfg.ini")
    print("Dolphin.ini path: " + app_config["PATHS"]["dolphin_settings"])
    dolphin_config.read(app_config["PATHS"]["dolphin_settings"])

    print("Dolphin.ini sections:")
    print(dolphin_config.sections())
    try:
        subprocess.run(["wit", "list", dolphin_config["General"]["ISOPath0"]], check=True, text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n*** Wiimms ISO Tools not found! ***\nDownload it from here:\nhttps://wit.wiimm.de")