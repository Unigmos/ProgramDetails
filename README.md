# ProgramDetails
ファイルの行数や詳細を表示するプログラムです

## 使用ライブラリ
| 使用ライブラリ | 使用目的 |
| :--- | :--- |
| glob | ファイル探索 |
| os | ファイル情報取得 |
| pandas | データフレーム構築 |
| streamlit | Web画面表示 |
| matplotlib | グラフ描画 |
| japanize_matplotlib | matplotlibの日本語対応 |

## 実行結果サンプル
実行すると以下のような画面のブラウザが表示されます。
<img src="https://user-images.githubusercontent.com/77985354/212237660-d3309c37-a9a6-44b8-869c-827f39cfa9b6.png" width="450px">
<img src="https://user-images.githubusercontent.com/77985354/212237672-61f3befe-2ca7-4d5b-8d8f-0c14d8e5bca0.png" width="450px">

## 実行にあたって
以下の順にプロンプトを実行することでブラウザ画面に表示することができます。<br>
```
rem プログラムの保存場所まで移動
cd C:\XXX\XXX\src

rem データ収集用のプログラム実行
python aggregate.py

rem ブラウザ画面に表示
streamlit run page.py
```
