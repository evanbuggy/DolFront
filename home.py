# This is the home page for the app.

from nicegui import ui
import configparser, os, subprocess, glob

config = configparser.ConfigParser()
config.read("cfg.ini")
config.read(config["PATHS"]["dolphin_user_path"])

subprocess.run("wit")

ui.button("Open Dolphin", on_click=lambda: subprocess.Popen(config["PATHS"]["dolphin_path"]))

ui.run(native=True, window_size=(400, 300), fullscreen=False)
