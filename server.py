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
    print("data:%s", data)
    return {"message": "データが正常に受信されました", "data": data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
