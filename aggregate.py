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
    import subprocess

    # パスファイル名
    text_path = "path.txt"
    # 除外する拡張子
    excp_list = [".aup",".png",".jpg",".wav",".mp3",".mp4",".txt"]

    # パスの読み込み
    def get_path(name):
        with open(name) as f:
            path_name = f.readline().rstrip()
        return path_name

    # ファイルデータの取得
    def get_file_data(path):
        for file_path in glob.glob(path + "/**/*"):
            file_name = os.path.split(file_path)[1]
            _, extension = os.path.splitext(file_name)
            # ファイルの有無を確認することでディレクトリ名だけのパスを除外する
            # また、動画ファイルなど行数が測定できないファイルを除外する
            if os.path.isfile(file_path) and extension not in excp_list:
                #print(extension)
                print(f"path:{file_path}")
                print(f"name:{file_name}")
                print(f"size:{os.path.getsize(file_path)}")
                with open(file_path) as lf:
                    lines = sum([1 for line in lf])
                print(f"lines:{lines}\n")

    path_data = get_path(text_path)
    #print(path_data)
    get_file_data(path_data)

    # HTMLファイルを開く
    #webbrowser.open("index.html")

if __name__ == '__main__':
    main()