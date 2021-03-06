import toml
# pip install toml for this package to work

import os
from sys import exit
from tkinter import Tk
from tkinter import messagebox

config_toml = """# This is the directory to be sorted into the corresponding folders.
# Input must be a directory e.g C:/Users/Username/Downloads
# Please be aware that '\\' will not work for the directory unless '\\\\' is used instead.

sorting_dir = ''

# This will sort any non-ignored file types into a miscellaneous folder.
# Input must be true/false
misc_enabled = false

# These file extensions will be ignored.
ignore = [
    'ini'
]

# These are the folders to be sorted into, based on the file extensions input.
# To create a new folder, follow the format below.
[folders]
Images = [
    'jpg',
    'jpeg',
    'png',
    'gif',
    'bmp'
]

Videos = [
        'webm',
        'mp4',
        'avi',
        'mov',
        'mkv',
        'm4v'
]"""

if not os.path.exists('config.txt'):
    with open('config.txt', 'w') as x:
        x.write(config_toml)
        Tk().withdraw()
        messagebox.showinfo(title="Config Created",
                            message="Config file has been created.\n"
                                    "Please input your sorting directory into the config and run the program again.")
        exit()

try:
    data = toml.loads(open('config.txt', 'r').read())
    misc_enabled = data["misc_enabled"]
    ignored_extensions = data["ignore"]
    folders = data["folders"]
    sorting_dir = data["sorting_dir"]
    if not os.path.exists(sorting_dir):
        Tk().withdraw()
        messagebox.showerror(title="Config Error",
                             message="Sorting directory is empty or does not exist.\n"
                                     "Please check your config file and try again.")
        exit()

except toml.decoder.TomlDecodeError:
    Tk().withdraw()
    messagebox.showerror(title="Config Error",
                         message="There is likely to be an issue with your sorting directory input.\n"
                                 "Please check your config file and try again.")
    exit()

except KeyError:
    Tk().withdraw()
    messagebox.showerror(title="Config Error",
                         message="A required option is missing or renamed.\n"
                                 "Please check your config file and try again.")
    exit()
