import os
import pandas as pd

from header_info import CUSTOMER_MASTER_FILE_SCHEMA_LIST
from header_info import FUND_MASTER_FILE_SCHEMA_LIST

target_dir_path = './csv_files'
result_dir_path = './converted_csv_files'


def read_csv(file_path, header_list, encoding='utf-8'):
    return pd.read_csv(file_path, names=header_list, dtype=str, encoding=encoding)


def to_csv(df, file_path, header=False, index=False, encoding='utf-8'):
    df.to_csv(file_path, header=header, index=index, encoding=encoding)


def get_file_path(dir_path, file_name):
    return dir_path + '/' + file_name


def get_first_row(df):
    return df[:1]


def convert_kokyaku_master(file_name):
    target_file_path = get_file_path(target_dir_path, file_name)
    file_base_name = os.path.splitext(file_name)[0]

    # ヘッダーを追加してcsv読み込み
    header_list = [column_info.get('name') for column_info in CUSTOMER_MASTER_FILE_SCHEMA_LIST]
    csv_data_df = read_csv(target_file_path, header_list)

    # 項目数エラーのcsv作成 002
    target_df = get_first_row(csv_data_df)
    # TODO 自分で作成する？
    result_file_path = get_file_path(result_dir_path, file_base_name + '_002.csv')
    to_csv(target_df, result_file_path)

    # 99999999から99991231に読み替え 003
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(TE01E=['99999999'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_003.csv')
    to_csv(target_df, result_file_path)

    # date型カラムの変換エラー 004
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(TE01E=['ABCDEFGH'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_004.csv')
    to_csv(target_df, result_file_path)

    # dateが99991232の場合、型バリデーションエラー 005
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(TE01E=['99991232'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_005.csv')
    to_csv(target_df, result_file_path)

    # 時刻データの範囲(date) 006
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(TE01E=['18991231'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_006.csv')
    to_csv(target_df, result_file_path)

    # datetime型カラムの時刻データ変換 007
    date_column_list = ['TA03B']
    for date_column in date_column_list:
        target_df = get_first_row(csv_data_df)
        target_df = target_df.assign(**{date_column: ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']})
        result_file_path = get_file_path(result_dir_path, file_base_name + '_007.csv')
        to_csv(target_df, result_file_path)

    # 重複エラー 008
    target_df = get_first_row(csv_data_df)
    target_df = target_df.append(target_df)
    result_file_path = get_file_path(result_dir_path, file_base_name + '_008.csv')
    to_csv(target_df, result_file_path)

    # 文字コードがshift-jis 009
    target_df = get_first_row(csv_data_df)
    result_file_path = get_file_path(result_dir_path, file_base_name + '_009.csv')
    to_csv(target_df, result_file_path, encoding='shift_jis')


def convert_fund_master(file_name):
    target_file_path = get_file_path(target_dir_path, file_name)
    file_base_name = os.path.splitext(file_name)[0]

    # ヘッダーを追加してcsv読み込み
    header_list = [column_info.get('name') for column_info in FUND_MASTER_FILE_SCHEMA_LIST]
    csv_data_df = read_csv(target_file_path, header_list)

    # 項目数エラーのcsv作成 002
    target_df = get_first_row(csv_data_df)
    # TODO 自分で作成する？
    result_file_path = get_file_path(result_dir_path, file_base_name + '_002.csv')
    to_csv(target_df, result_file_path)

    # 99999999から99991231に読み替え 003
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(TE01E=['99999999'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_003.csv')
    to_csv(target_df, result_file_path)

    # date型カラムの時刻データ変換 004
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(TE01E=['ABCDEFGH'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_004.csv')
    to_csv(target_df, result_file_path)

    # dateが99991231の場合、型バリデーションエラー 005
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(TE01E=['99991232'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_005.csv')
    to_csv(target_df, result_file_path)

    # 時刻データの範囲(date) 006
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(TE01E=['18991231'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_006.csv')
    to_csv(target_df, result_file_path)

    # datetime型カラムの時刻データ変換 007
    date_column_list = ['TA03B']
    for date_column in date_column_list:
        target_df = get_first_row(csv_data_df)
        target_df = target_df.assign(**{date_column: ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']})
        result_file_path = get_file_path(result_dir_path, file_base_name + '_007.csv')
        to_csv(target_df, result_file_path)

    # コード妥当性チェック KO012 008
    # ### KO012 accounting_standards
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(KO012=['&'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_008.csv')
    to_csv(target_df, result_file_path)

    # コード妥当性チェック KE0P2 009
    # ### KE0P2 genshintaku_jutakusha_class
    target_df = get_first_row(csv_data_df)
    target_df = target_df.assign(KE0P2=['&&'])
    result_file_path = get_file_path(result_dir_path, file_base_name + '_009.csv')
    to_csv(target_df, result_file_path)

    # 重複エラー 010
    target_df = get_first_row(csv_data_df)
    target_df = target_df.append(target_df)
    result_file_path = get_file_path(result_dir_path, file_base_name + '_010.csv')
    to_csv(target_df, result_file_path)

    # 文字コードがshift-jis 011
    target_df = get_first_row(csv_data_df)
    result_file_path = get_file_path(result_dir_path, file_base_name + '_011.csv')
    to_csv(target_df, result_file_path, encoding='shift_jis')


def main():

    for file_name in os.listdir(target_dir_path):

        if file_name == 'fmk_kokyaku_master.csv':
            convert_kokyaku_master(file_name)

        if file_name == 'fmk_fund_master.csv':
            convert_fund_master(file_name)


if __name__ == '__main__':
    main()
