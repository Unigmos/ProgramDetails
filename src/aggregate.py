#-------------------------------------------------------------------------------
# Name:         aggregate
# Purpose:      ファイル情報を取得しCSVに保存
#
# Author:       Shaneron
#
# Created:      11/01/2023
# Copyright:    (c) Shaneron 2023
#-------------------------------------------------------------------------------

def main():
    import glob
    import os
    import pandas as pd

    # パスファイル名
    text_path = "path.txt"
    # csvファイル名
    csv_path = "data.csv"

    # パスの読み込み
    def get_path(name):
        with open(f"../{name}") as f:
            path_name = f.readline().rstrip()
        return path_name

    # ファイルデータの取得,JSONに保存
    def get_file_data(path):
        total_lines = 0
        df_path = []
        df_name = []
        df_extension = []
        df_size = []
        df_lines = []
        for file_path in glob.glob(f"{path}/**/*.*", recursive=True):
            # ファイル名
            file_name = os.path.split(file_path)[1]
            # ファイルの拡張子
            _, file_extension = os.path.splitext(file_path)
            # ファイルのサイズ
            file_size = os.path.getsize(file_path)

            # 行数が測定できないデータはlinesを0に設定
            try:
                df_path.append(file_path)
                df_name.append(file_name)
                df_extension.append(file_extension)
                df_size.append(file_size)
                print(f"path:{file_path}")
                print(f"name:{file_name}")
                print(f"extension:{file_extension}")
                print(f"size:{file_size}")
                with open(file_path) as lf:
                    file_lines = sum([1 for line in lf])
                print(f"lines:{file_lines}\n")
                total_lines += int(file_lines)

                df_lines.append(file_lines)

            except UnicodeDecodeError:
                file_lines = 0
                df_lines.append(0)

        df = pd.DataFrame(
            {
                "path": df_path,
                "name": df_name,
                "extension": df_extension,
                "size": df_size,
                "lines": df_lines,
            })

        df.to_csv(f"../output/{csv_path}", index=False)
        print(total_lines)

    path_data = get_path(text_path)
    get_file_data(path_data)

if __name__ == '__main__':
    main()
