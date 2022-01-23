import os
import json
# from db.base_engine import execute_raw_sql, get_db_engine
from util.util import dump_execution_point
from util.logger import Logger
import subprocess
import requests
import xmltodict
import paramiko

log = Logger('/')


# テスト用のlambdaの為、商用で利用されることはない。
def handler(event, context):
    # 2022/1/11 COCOA導通試験
    response = requests.get("https://test.connect.auone.jp/net/vwc/cca_lg_eu_nets/login?targeturl=a")
    print(response)

    # # 2021/12/23 JEWELRY導通試験
    # print("2021/12/23 JEWELRY導通試験")
    # HOST = os.environ.get('SFTP_HOST')
    # PORT = os.environ.get('SFTP_PORT')
    # USER = os.environ.get('SFTP_USER')
    # PASSWORD = os.environ.get('SFTP_PASSWORD')

    # with paramiko.SSHClient() as sftp_client:
    #     sftp_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    #     sftp_client.connect(HOST, port=PORT, username=USER, password=PASSWORD)

    #     sftp_connection = sftp_client.open_sftp()

    # # 2021/12/23 auMarket導通試験 NW試験
    # print('2021/12/23 auMarket導通試験 NW試験')
    # result = subprocess.run(["openssl", "s_client", "-connect", "spmk1b-exelb-fgif001-646956968.ap-northeast-1.elb.amazonaws.com:443"], stdout=subprocess.PIPE)
    # print(result.stdout.decode("utf-8"))

    # # 2021/12/23 auMarket導通試験 IF試験
    # print("2021/12/23 auMarket導通試験 IF試験")
    # url = "https://spmk1b-exelb-fgif001-646956968.ap-northeast-1.elb.amazonaws.com:443/moutside/UserHistory?carrier=KDDI&if_version=1"
    # lid = "kddi_b2gilm7velmeb20390302102218"
    # service_id = "10001"
    # member_id = os.environ.get('AU_MARKET_USER_HISTORY_ID')
    # member_item = member_id + '00000001'

    # data = """
    #     <history_req>\r\n
    #         <p_no>20140819193084958697</p_no>\r\n
    #         <auoneId>{system_au_id}</auoneId>\r\n
    #         <memberId>{member_id}</memberId>\r\n
    #         <serviceId>{service_id}</serviceId>\r\n
    #         <memberItemCd>{member_item}</memberItemCd>\r\n
    #     </history_req>\r\n
    # """.format(system_au_id=lid, service_id=service_id, member_id=member_id, member_item=member_item)
    # datas = data.strip().encode('shift-jis')
    # headers = {
    #     'Content-Type': 'text/xml; charset=shift-jis',
    #     'Content-Length': str(len(datas))
    # }

    # # ### verify=False
    # result = requests.post(url, data=data, headers=headers, timeout=9.0)
    # result.encoding = result.apparent_encoding
    # result_dict = xmltodict.parse(result.text)
    # print(result_dict)

    return

# def get_sample():

#     query = '''

#         SELECT * FROM in_application_history;

#     '''

#     try:

#         engine = get_db_engine()

#         with engine.begin() as conn:
#             result = execute_raw_sql(conn, query)

#         return [dict(row) for row in result]

#     except Exception as e:
#         log.error(dump_execution_point())
#         log.error(e)
#         raise Exception()
