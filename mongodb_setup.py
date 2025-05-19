from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["o2ocom_db"]
collections = ["sales", "efficiency", "tokens"]
for name in collections:
    if name not in db.list_collection_names():
        db.create_collection(name)
        print(f"✅ Created collection: {name}")
    else:
        print(f"✔️ Collection already exists: {name}")
db["efficiency"].create_index("user_id", unique=True)
db["tokens"].create_index("user_id", unique=True)
print("🎉 MongoDB setup completed for o2ocom_db")
