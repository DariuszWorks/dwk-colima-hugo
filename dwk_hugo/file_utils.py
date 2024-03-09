import os
import shutil


def clean_folder(folder_path: str):
    """
    Clean a folder by removing all its contents and creating a new empty folder.

    :param folder_path: The path of the folder to be cleaned.
    :return: None
    """
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.makedirs(folder_path)
    except OSError as e:
        print("Error: %s : %s" % (folder_path, e.strerror))
