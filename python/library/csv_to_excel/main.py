import os
import pandas as pd
from table_type import data_type

csv_dir_path = "./csv_files"
excel_dir_path = "./excel_files"
integrated_file_path = "./excel_files/integrated_data.xlsx"


def add_sheet_to_excel(file_path, csv_data, sheet_name, excel_index=False):
    with pd.ExcelWriter(file_path, engine="openpyxl", mode="a") as f:
        csv_data.to_excel(f, sheet_name=sheet_name, index=excel_index, encoding='cp932')


def create_integrated_excel(file_path, csv_data, sheet_name, excel_index=False):
    csv_data.to_excel(file_path, sheet_name=sheet_name, index=excel_index, encoding='cp932')


def convert_csv_to_individual_excel(csv_data, file_name):
    excel_file_path = excel_dir_path + "/" + file_name + ".xlsx"
    csv_data.to_excel(excel_file_path, sheet_name=file_name, index=False, encoding='cp932')


def read_csv(file_name, ext=True):
    csv_file_path = csv_dir_path + "/" + file_name if ext else csv_dir_path + "/" + file_name + ".csv"
    return pd.read_csv(csv_file_path, dtype=data_type.get(file_name))


def main(mode):
    file_name_list = [os.path.splitext(os.path.basename(file_name))[0] for file_name in os.listdir(csv_dir_path)]

    for file_name in file_name_list:
        if file_name == ".DS_Store":
            continue

        csv_data = read_csv(file_name, ext=False)

        if mode == "individual" or "":
            convert_csv_to_individual_excel(csv_data, file_name)
        else:
            add_sheet_to_excel(integrated_file_path, csv_data, file_name) \
                if os.path.isfile(integrated_file_path) else \
                create_integrated_excel(integrated_file_path, csv_data, file_name)


if __name__ == "__main__":
    input_mode = input("integration or individual: ")

    if input_mode not in ["integration", "individual", ""]:
        print("不正な入力")
        exit()

    main(input_mode)
