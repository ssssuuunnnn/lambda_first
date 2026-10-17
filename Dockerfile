FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 安裝系統相依工具（若有需要編譯套件時會用到）
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# 預先升級 pip
RUN pip install --no-cache-dir --upgrade pip
