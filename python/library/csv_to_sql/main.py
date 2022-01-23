import os
import pandas as pd

csv_files_path = "../csv_to_excel/csv_files"


def main():

    for file_name in os.listdir(csv_files_path):
        df = pd.read_csv(csv_files_path + "/" + file_name, engine="python")
        print(df.dtypes)


if __name__ == "__main__":
    main()
