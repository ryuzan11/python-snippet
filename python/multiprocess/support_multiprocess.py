import time
import requests

from multiprocessing import Process, Pipe
from more_itertools import chunked


def parallelize(func_setting_list, split=3):

    result_dict = {}

    split_list = list(chunked(func_setting_list, split))

    for target in split_list:
        result_dict = {**result_dict, **execute_parallelize(target)}

    return result_dict


def wrapped_func(*args, **kwargs):
    conn = args[0]
    func = args[1]

    try:
        result = func(*args[2:], **kwargs)
    except Exception as e:
        result = None

    conn.send(result)
    conn.close()


def execute_parallelize(func_setting_list):

    process_list = []

    for setting in func_setting_list:

        parent_conn, child_conn = Pipe()

        func_key = setting.get('func_key')
        func = setting.get('func')

        process = Process(target=wrapped_func, args=(child_conn, func, *setting.get('args'), ), kwargs=setting.get('kwargs'))
        process.start()

        process_list.append({'func_key': func_key, 'parent_conn': parent_conn, 'process': process})

    for process in process_list:
        process.get('process').join()

    return {process.get('func_key'): process.get('parent_conn').recv() for process in process_list}


def get_func_setting(func_key, func, args, kwargs=None):

    return {
        'func_key': func_key,
        'func': func,
        'args': args,
        'kwargs': kwargs if kwargs else {}
    }


def support_method(count):
    count_i = 0
    for i in range(count):
        count_i += i
    return count_i


def not_return(arg):
    convert_arg = '{}/sample'.format(arg)


def not_use_multiprocess():
    start = time.time()
    r_get1 = requests.get('https://github.com/timeline.json')
    r_get2 = requests.get('https://github.com/timeline.json')
    r_get3 = requests.get('https://github.com/timeline.json')
    r_get4 = requests.get('https://github.com/timeline.json')
    end = time.time()
    elapsed_time = end - start
    print('スタート => ', start)
    print('終わり => ', end)
    print('処理時間 => ', elapsed_time)
    print('r_get1の処理結果 => ')
    print(r_get1.text)


def use_multiprocess():
    # threadもしくはprocessが呼び出せる関数でなければ実行できないため、getメソッドを変数に格納する
    # 内部関数はその関数を含む外部関数の中からしか呼び出せない
    arg = 'https://github.com/timeline.json'
    start = time.time()
    result = parallelize([
        get_func_setting('sample1', requests.get, (arg,)),
        get_func_setting('sample2', requests.get, (arg,)),
        get_func_setting('sample3', requests.get, (arg,)),
        get_func_setting('sample4', requests.get, (arg,))
        # returnなし関数の場合、Noneが返る(textはエラーになる)
        # get_func_setting('sample1', not_return, (arg,))
    ])
    end = time.time()
    elapsed_time = end - start
    print('スタート => ', start)
    print('終わり => ', end)
    print('処理時間 => ', elapsed_time)
    print('sample1の処理結果 => ')
    print(result.get('sample1').text)
