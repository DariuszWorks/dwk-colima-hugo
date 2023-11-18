import os
import shutil


def clean_folder(folder_path: str):
    """Clean folder by removing its content and creating it again.

    :param folder_path:
    """
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.makedirs(folder_path)
    except OSError as e:
        print("Error: %s : %s" % (folder_path, e.strerror))