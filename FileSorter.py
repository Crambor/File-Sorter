from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import re
import os
import time
import config


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(config.sorting_dir):
            if '.' not in filename:
                continue

            name, extension = filename.rsplit('.', 1)
            if extension in config.ignored_extensions:
                continue

            try:
                folder_dir = f'{config.sorting_dir}\\' + self.get_folder(extension)
            except TypeError:
                continue

            if not os.path.isdir(folder_dir):
                os.mkdir(folder_dir)

            try:
                self.move_file(name, extension, folder_dir)
            except PermissionError:
                continue

    @staticmethod
    def get_folder(extension):
        for folder in config.folders:
            if extension in config.folders[folder]:
                return folder

        if config.misc_enabled:
            return 'Misc'
        return None

    @staticmethod
    def move_file(name, extension, folder_dir):
        def is_file(folder_file):
            return bool(re.match(fr'{name}.{extension}|{name}(\s\(([0-9]+)\)\.)', folder_file))

        files = sorted(filter(is_file, os.listdir(folder_dir)))
        files = files[-1:] + files[:-1]

        if files[:1] != [f"{name}.{extension}"]:
            filename = f"{name}.{extension}"
        else:
            i = 2
            for file in files[1:]:
                num = int(re.search(r'\s\(([0-9]+)\)\.', file).group(1))
                if i != num:
                    break

                i += 1

            filename = f"{name} ({i}).{extension}"

        src = f"{config.sorting_dir}\\{name}.{extension}"
        dst = f"{folder_dir}\\{filename}"
        os.rename(src, dst)


event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, config.sorting_dir, recursive=False)
observer.start()

print("Successfully initialised")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
