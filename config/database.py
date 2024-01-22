from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.fastapi

collection_user = db["user_collection"]
collection_role = db["role_collection"]