import configparser, os, subprocess
from nicegui import ui

new_config = configparser.ConfigParser()
dolphin_path: str = ""
dolphin_settings: str = ""
covers_path: str = ""

def set_text(s: str, n: str):
    s = n

# Dolphin Path
ui.input(label="Dolphin Path", placeholder="This is the path for Dolphin.exe.", on_change=lambda e: set_text(dolphin_path, e.value))

# Covers Path
ui.input(label="Covers Path", placeholder="This is the path for images of game covers.", on_change=lambda e: set_text(covers_path, e.value))

# Dolphin Settings Path
ui.input(label="Dolphin Settings", placeholder="This is the path for Dolphin.cfg. It's most likely found in your Documents folder on Windows.", on_change=lambda e: set_text(dolphin_settings, e.value))