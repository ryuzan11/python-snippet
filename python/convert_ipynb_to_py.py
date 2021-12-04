import sys
import shutil
import subprocess

from util.file import get_filepath_list

PY_PATH = '../jupyter_notebook/*.py'


def main(pathname_list):

    # TODO コマンドライン引数を設定した場合の処理を今後追加
    if len(pathname_list) > 0:
        raise Exception()

    subprocess.run(['jupyter', 'nbconvert', '--to', 'python', '../jupyter_notebook/*.ipynb'])

    move_py_file(PY_PATH)

    return


def move_py_file(target_folder_path, destination_path='jupyter_to_py'):
    for target_filepath in get_filepath_list(target_folder_path):
        shutil.move(target_filepath, destination_path)


if __name__ == '__main__':
    args = sys.argv[1:]

    main(args)
