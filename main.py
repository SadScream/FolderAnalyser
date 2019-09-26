import os

file_extensions = [""]


class Handler:
    __slots__ = ("data_files", "data_folders")

    def __init__(self):
        self.data_files = [] # out data
        self.data_folders = []

    def analyse_files(self, folders):
        for item in folders:
            for file in __getFiles__(item):
                self.data_files.append(file)
            self.analyse_files(__getFolders__(item))

    def analyse_folders(self, folders):
        for item in folders:
            for file in __getFolders__(item):
                self.data_folders.append(file)
            self.analyse_folders(__getFolders__(item))


def __getFiles__(folder):
    try:
        files = [os.path.join(folder, file) for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file)) and any(ext in file for ext in file_extensions)]
    except FileNotFoundError:
        return ("System cannot find the path")
    except TypeError:
        return ("Path type error")
    except Exception as E:
        return (f"Exception: {E}")
    else:
        return files

def __getFolders__(folder):
    try:
        files = [os.path.join(folder, file) for file in os.listdir(folder) if os.path.isdir(os.path.join(folder, file))]
    except FileNotFoundError:
        return ("System cannot find the path")
    except TypeError:
        return ("Path type error")
    except Exception as E:
        return (f"Exception: {E}")
    else:
        return files


def main(p, mode=1):

    '''
    :mode: - bool; 1 - finds files, 0 - finds folders
    '''
    data_files = []
    folders_in_parent = []
    text = os.path.join(p, "") # "C:\\Python\\Development\\FolderAnalyser"

    if mode in [1, True]:
        files = __getFiles__(text)
        if any(item in files for item in ["System cannot find the path", "Path type error", "Exception:"]):
            return files
        for item in files:
            data_files.append(item)

    folders = __getFolders__(text)
    if any(item in folders for item in ["System cannot find the path", "Path type error", "Exception:"]):
        return folders
    for item in folders:
        folders_in_parent.append(item)

    handler = Handler()

    if mode in [1, True]:
        handler.analyse_files(folders_in_parent)
        for item in handler.data_files:
            data_files.append(item)
        return data_files

    elif mode in [0, False]:
        handler.analyse_folders(folders_in_parent)
        for item in handler.data_folders:
            folders_in_parent.append(item)
        return folders_in_parent



class App:

    def app(self, p, t=1):
        """0 - нахождение папок, 1 - нахождение файлов"""

        if t not in [0, 1, True, False]:
            return None
        elif not os.path.isdir(p):
            return None
        else:
            return main(p, t)