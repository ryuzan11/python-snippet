import argparse
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--delay', type=str, default='1')
parser.add_argument('-s', '--status', type=str, default='500')
parser.add_argument('-sl', '--statusList', type=list, default=[500, 501, 502, 503], nargs='*')


def main(args):

    # 遅延処理
    delay_time = args.arg1

    delay_time_url = 'https://httpbin.org/delay/{}'.format(delay_time)

    rs_delay_time = requests.Session()

    retries = Retry(total=2, backoff_factor=1)

    rs_delay_time.mount('https://', HTTPAdapter(max_retries=retries))

    delay_time_result = rs_delay_time.request('GET', delay_time_url, timeout=2.0)

    print(delay_time_result)

    # ステータスコード
    status_code = args.arg2
    status_code_list = args.arg3

    status_code_url = 'https://httpbin.org/status/{}'.format(status_code)
    status_force_list = status_code_list

    rs_status = requests.Session()

    retries = Retry(total=2, backoff_factor=1, status_forcelist=status_force_list)

    rs_status.mount('https://', HTTPAdapter(max_retries=retries))

    status_result = rs_status.request('GET', status_code_url, timeout=2.0)

    print(status_result)

    return


# python main.py -d 5 -s 500 -sl [400, 401]
if __name__ == '__main__':

    # TODO ifで遅延かステータスかで関数選べたらいいかも
    input_args = parser.parse_args()

    main(input_args)
