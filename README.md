# streamlit_tailwind_form

このプロジェクトは、Streamlitを使用してフォームを作成し、Tailwind CSSでスタイルを適用し、そのデータをFastAPIバックエンドサーバにPOSTリクエストとして送信する方法をデモンストレーションしています。

## プロジェクト構成

- `app.py`: Streamlitアプリケーション。フォームを作成し、バックエンドサーバにデータを送信します。
- `server.py`: FastAPIバックエンドサーバ。POSTリクエストを受信して処理します。

## 前提条件

以下のパッケージがインストールされている必要があります。

- Python 3.7+
- Streamlit
- FastAPI
- Uvicorn
- Requests

必要なパッケージを以下のコマンドでインストールできます。

```bash
pip install streamlit fastapi uvicorn requests
```

## 実行手順

### ステップ 1: FastAPI バックエンドサーバの起動

以下のコマンドでFastAPIサーバを起動します。

```bash
python server.py
```

サーバは `http://localhost:8000` で起動します。

### ステップ 2: Streamlit アプリケーションの起動

別のターミナルで、以下のコマンドを実行してStreamlitアプリケーションを起動します。

```bash
streamlit run app.py
```

これにより、Streamlitアプリケーションが起動し、`http://localhost:8501` でアクセス可能になります。

## コード詳細

### Streamlit アプリケーション (app.py)

Streamlitを使用して、フォームを作成し、入力されたデータをローカルホストのバックエンドサーバにPOSTリクエストとして送信します。

```python
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
```

### FastAPI バックエンドサーバ (server.py)

FastAPIを使用して、POSTリクエストを受信し、受信したデータをJSON形式で返すサーバを構築します。

```python
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# POSTリクエストのデータモデルを定義
class FormData(BaseModel):
    name: str
    age: int
    gender: str

# POSTリクエストを受信するエンドポイント
@app.post("/submit")
async def submit_form(data: FormData):
    # 受信したデータを表示
    return {"message": "データが正常に受信されました", "data": data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## 使用方法

1. `server.py`を実行してバックエンドサーバを起動します。
2. 別のターミナルで、`app.py`を実行してStreamlitアプリケーションを起動します。
3. ブラウザで `http://localhost:8501` にアクセスし、フォームに入力して送信ボタンを押すと、データが`localhost:8000/submit`に送信されます。

このプロジェクトでは、フロントエンドのスタイリングにTailwind CSSを使用し、バックエンドとの通信にFastAPIを使用することで、シンプルで効率的なWebアプリケーションを構築しています。
```

このREADME.mdは、プロジェクトのセットアップから実行方法、コードの詳細までを網羅しており、他の開発者や将来の自分がプロジェクトの内容を理解するのに役立ちます。
