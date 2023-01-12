#-------------------------------------------------------------------------------
# Name:         aggregate
# Purpose:      ファイル情報を取得しJSONに保存
#
# Author:       Shaneron
#
# Created:      11/01/2023
# Copyright:    (c) Shaneron 2023
#-------------------------------------------------------------------------------

def main():
    import webbrowser
    import glob
    import os
    import json

    # パスファイル名
    text_path = "path.txt"
    # jsonファイル名
    json_path = "data.json"

    # パスの読み込み
    def get_path(name):
        with open(name) as f:
            path_name = f.readline().rstrip()
        return path_name

    # ファイルデータの取得,JSONに保存
    def get_file_data(path):
        total_lines = 0
        json_data = {}
        json_data["search_path"] = path
        json_data["files"] = []
        for file_path in glob.glob(path + "/**/*.*", recursive=True):
            # ファイル名
            file_name = os.path.split(file_path)[1]
            # ファイルのサイズ
            file_size = os.path.getsize(file_path)
            # 行数が測定できないデータはlinesを0に設定
            try:
                print(f"path:{file_path}")
                print(f"name:{file_name}")
                print(f"size:{file_size}")
                with open(file_path) as lf:
                    file_lines = sum([1 for line in lf])
                print(f"lines:{file_lines}\n")
                total_lines += int(file_lines)
            except UnicodeDecodeError:
                file_lines = 0

            # jsonに書き込む用のデータの追加
            json_data["files"].append({
                "path": file_path,
                "name": file_name,
                "size": file_size,
                "lines": file_lines,
            })

        # jsonファイルに書き込み
        with open(json_path, "w") as jf:
            json.dump(json_data, jf, indent=4)


        print(total_lines)

    path_data = get_path(text_path)
    get_file_data(path_data)

    # HTMLファイルを開く
    #webbrowser.open("index.html")

if __name__ == '__main__':
    main()