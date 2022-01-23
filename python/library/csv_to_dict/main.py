import csv
import json

csv_file = open("csv_data.csv", "r", encoding="utf_8", errors="", newline="")
table_info = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

# fund_list = list()
date_no_list = [4, 5, 8, 9, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 69]

for i, column_info in enumerate(table_info):
    no = i + 1

    column_info_list = column_info[0].split()

    column_name = column_info_list[0]
    column_type = column_info_list[1].split("(")[0]
    converted_column_type = "date" if no in date_no_list else "str" if column_type == "varchar" else column_type
    column_size = int(column_info_list[1].split("(")[1][:-1])
    converted_column_size = 26 if no == 70 else column_size
    is_last = True if no == 70 else False

    new_column_info = {
        "name": column_name,
        "type": converted_column_type,
        "size": converted_column_size,
        "is_last": is_last
    }

    file_path = "dict_data.py"
    with open(file_path, mode='a') as f:
        f.write("\r\n" + json.dumps(new_column_info))
