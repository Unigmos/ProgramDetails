#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shaneron
#
# Created:     13/01/2022
# Copyright:   (c) Shaneron 2022
#-------------------------------------------------------------------------------

def main():
    import streamlit as st
    import pandas as pd
    from pandas.errors import EmptyDataError
    import matplotlib.pyplot as plt
    import japanize_matplotlib

    # csvファイル名
    csv_path = "data.csv"

    st.title("ProgramDetails")
    st.caption("指定した階層以下のコードの行数やサイズの詳細を可視化するアプリです。")

    st.header("全体評価")

    # データが存在しなかったとき用の空のデータ定義
    exc_df = pd.DataFrame(
            {
                "path": [" "],
                "name": [" "],
                "extension": [" "],
                "size": [" "],
                "lines": [" "],
            })

    try:
        df = pd.read_csv(f"../output/{csv_path}")
    except EmptyDataError:
        df = exc_df
    except FileNotFoundError:
        df = exc_df

    # グラフ描画用のデータフレーム構築
    extension_group = df.groupby("extension").sum()
    sort_df = extension_group.sort_values("lines", ascending=False)
    line_df = sort_df.drop("size", axis=1)
    size_df = sort_df.drop("lines", axis=1)

    st.text("取得データ")
    st.dataframe(df, 700, 500)
    st.text(f"容量:{df['size'].sum()}")
    st.text(f"行数:{df['lines'].sum()}")

    st.header("拡張子別の評価")

    # 横並び
    column_1, column_2 = st.columns(2)
    with column_1:
        st.text("拡張子別の合計値")
        st.table(sort_df)

    with column_2:
        # グラフ描画
        fig, ax = plt.subplots()
        ax.bar(line_df.index, line_df["lines"])
        ax.set_xlabel("拡張子")
        ax.set_ylabel("行数")
        ax.set_title("拡張子別の行数比較")
        st.pyplot(fig)

        fig, ax = plt.subplots()
        ax.bar(size_df.index, size_df["size"])
        ax.set_xlabel("拡張子")
        ax.set_ylabel("データサイズ")
        ax.set_title("拡張子別のデータサイズ比較")
        st.pyplot(fig)


if __name__ == '__main__':
    main()
