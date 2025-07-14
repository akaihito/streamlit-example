"""
streamlit run simple_app.py
"""


import streamlit as st

#タイトル表示
st.title("簡単な streamlit アプリ")

#ユーザからテキスト入力を受け取る
name = st.text_input("あなたの名前を入力してください。")

# ユーザからスライダー入力を受け取る (最小値、最大値、デフォルト値)
age = st.slider("あなたの年齢を入力してください。", 0, 100, 25)

# 結果表示
if name:    # もし nemeの変数が空{null}ではなかったら
    st.write(f"こんにちは{name}さん！あなたは{age}歳ですね！")
    st.write(f"{age-5}歳に見えますけどね")
else:
    st.write("上記の入力欄に名前を入力してください。")