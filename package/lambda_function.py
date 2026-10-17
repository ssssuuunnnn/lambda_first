from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on AWS Lambda via Docker!"}


# Mangum 作為 FastAPI 與 AWS Lambda 事件之間的轉接橋樑
handler = Mangum(app)
~
