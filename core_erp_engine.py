from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "o2ocom_db")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
sales_col = db["sales"]
eff_col = db["efficiency"]
token_col = db["tokens"]

app = FastAPI(title="Core ERP Engine with MongoDB")

class SalesData(BaseModel):
    user_id: int
    total: float

class EfficiencyResult(BaseModel):
    user_id: int
    score: float
    valid: bool

class TokenRecord(BaseModel):
    user_id: int
    score: float
    status: str

@app.post("/core/validate")
def validate_sales(data: SalesData):
    if data.total <= 0:
        raise HTTPException(status_code=400, detail="Invalid total amount")
    score = min(100, data.total * 10)
    valid = score >= 10
    sales_col.insert_one(data.dict())
    eff_col.update_one({"user_id": data.user_id}, {"$set": {"score": score}}, upsert=True)
    return EfficiencyResult(user_id=data.user_id, score=score, valid=valid)

@app.post("/core/trigger_win")
def trigger_win(data: EfficiencyResult):
    if data.score > 80 and data.valid:
        token_col.update_one({"user_id": data.user_id}, {"$set": {"score": data.score, "status": "minted"}}, upsert=True)
        return TokenRecord(user_id=data.user_id, score=data.score, status="minted")
    return TokenRecord(user_id=data.user_id, score=data.score, status="not_qualified")

@app.get("/core/dashboard")
def dashboard():
    eff_data = {doc["user_id"]: doc["score"] for doc in eff_col.find()}
    token_data = {doc["user_id"]: doc["status"] for doc in token_col.find()}
    return {"efficiency_scores": eff_data, "tokens": token_data}
