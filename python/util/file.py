import os
import glob


def get_filepath_list(pathname='*'):
    return glob.glob(pathname)


def get_filename(filepath, without_ext):
    return os.path.splitext(os.path.basename(filepath))[0] if without_ext else os.path.basename(filepath)


def get_filename_list(path='*', without_ext=True):
    filepath_list = glob.glob(path)

    return [get_filename(filepath, without_ext) for filepath in filepath_list]
