# This is the file that is used to launch the app. It will also handle launch parameters.

from init import init

match init():
    case 1:
        print("cfg.ini not found!!!")
    case 2:
        print("Dolphin not found!!!")
    case 3:
        print("WIT not found!!!")
    case 0:
        print("Everything seems OK!!!")