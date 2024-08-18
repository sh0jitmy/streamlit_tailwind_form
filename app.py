import streamlit as st
import requests

# Tailwind CSSのCDNリンクを追加
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        .stTextInput > div > input {
            @apply block w-full p-3 rounded-md border-gray-300 focus:ring-indigo-500 focus:border-indigo-500;
        }
        .stNumberInput input {
            @apply block w-full p-3 rounded-md border-gray-300 focus:ring-indigo-500 focus:border-indigo-500;
        }
        .stRadio label {
            @apply inline-flex items-center mr-4;
        }
        .stButton button {
            @apply bg-indigo-600 text-white font-medium py-2 px-4 rounded-md hover:bg-indigo-700;
        }
    </style>
""", unsafe_allow_html=True)

# フォームの作成
with st.form(key='my_form'):
    name = st.text_input('名前')
    age = st.number_input('年齢', min_value=0, max_value=120)
    gender = st.radio('性別', ('男性', '女性', 'その他'))
    
    # フォームの送信ボタン
    submit_button = st.form_submit_button(label='送信')

# フォームの送信が行われた場合の処理
if submit_button:
    # 送信するデータを準備
    payload = {
        'name': name,
        'age': age,
        'gender': gender
    }

    # ローカルホストにPOSTリクエストを送信
    url = 'http://localhost:8000/submit'  # 送信先のURLを指定
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            st.success("データが正常に送信されました！")
        else:
            st.error(f"送信に失敗しました。ステータスコード: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"送信中にエラーが発生しました: {e}")
