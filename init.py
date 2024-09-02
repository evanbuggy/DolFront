# This file is used to initialise important things on startup.

# This includes reading the Dolphin directory, the Dolphin user directory, the game
# covers directory and user settings. It will handle accordingly if these are not found.

import configparser, os, subprocess

app_config = configparser.ConfigParser()
dolphin_config = configparser.ConfigParser()
user_app_data_dir = os.getenv('APPDATA')

def init() -> int:
    print("DolFront v0.1\nA Dolphin and WIT frontend.\nSource code: https://github.com/evanbuggy/DolFront")

    try:
        app_config.read("cfg.ini")
    except OSError:
        print("\n*** cfg.ini not found! ***\nCreating cfg.ini...")
        return 1
    
    print("Dolphin.ini path: " + app_config["PATHS"]["dolphin_settings"])
    try:
        dolphin_config.read(app_config["PATHS"]["dolphin_settings"])
    except OSError:
        print("\n*** Dolphin.cfg not found! ***\nDo you have Dolphin installed?\nDownload it from here:\nhttps://dolphin-emu.org/")
        return 2

    print("Dolphin.ini sections:")
    print(dolphin_config.sections())

    try:
        subprocess.run(["wit", "list", dolphin_config["General"]["ISOPath0"]], check=True, text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n*** Wiimms ISO Tools not found! ***\nDownload it from here:\nhttps://wit.wiimm.de")
        return 3
    
    return 0