# 🚀 O2OCom.AI - Core ERP Engine (FastAPI + MongoDB)

> Mô hình triển khai ERP tối giản theo kiến trúc Win-Lane Flow.

## 📦 Tính năng
- FastAPI REST API cho POS O2O
- MongoDB làm nền tảng lưu trữ đơn hàng, KPI và token thưởng
- Có thể triển khai ngay lên Railway (tích hợp sẵn Dockerfile)

## 🧪 Local Dev
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn core_erp_engine:app --reload
```

## 🌍 Triển khai trên Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

Thêm biến môi trường:
- MONGO_URI
- MONGO_DB

## 🔍 Test endpoint
- GET `/core/dashboard`
- POST `/core/validate`
- POST `/core/trigger_win`

MIT © 2024
