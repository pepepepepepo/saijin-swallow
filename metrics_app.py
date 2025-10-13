from fastapi import FastAPI, Request
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017")
db = client.masato_archive
collection = db.questions

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question")
    collection.insert_one({"question": question})
    return {"message": "誠人の問いが記録されました"}
