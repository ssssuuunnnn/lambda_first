import os
from functools import lru_cache

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from supabase import Client, create_client

app = FastAPI()


@lru_cache
def get_supabase_client() -> Client:
    url = os.environ["SUPABASE_URL"]
    key = os.environ["SUPABASE_KEY"]
    return create_client(url, key)


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on AWS Lambda via Docker!"}

@app.get("/a")
def read_root():
    return {"message": "a"}

@app.get("/b")
def read_root():
    return {"message": "b"}


@app.get("/users")
def read_users():
    try:
        response = get_supabase_client().table("users").select("*").execute()
    except KeyError:
        raise HTTPException(status_code=500, detail="Supabase 環境變數未設定")
    except Exception:
        raise HTTPException(status_code=500, detail="查詢 Supabase 失敗")
    return response.data


# Mangum 作為 FastAPI 與 AWS Lambda 事件之間的轉接橋樑
lambda_handler = Mangum(app)
