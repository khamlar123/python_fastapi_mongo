from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from config.database import collection_user
from models.user import Users
from schemas.user import list_users
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
router = APIRouter()


@router.get('/user',tags=["user"])
async def get_user():
    users = list_users(collection_user.find())
    response_data = {"message": "get user successfully", "data": users}
    return JSONResponse(content=response_data, status_code=201)

@router.post('/user', tags=["user"])
async def post_users(user: Users):
    collection = collection_user
    try:
        user = user.dict()
        result = await collection.insert_one(user)
    except Exception as e:
        print(e)
    response_data = {"message": "user created successfully", "data": 1}
    return JSONResponse(content=response_data, status_code=201) 

@router.put("/user/{id}/")
async def update_user(id:str, updated_data:Users):
    await collection_user.update_one({"_id":ObjectId(id)},{"$set": updated_data})
    return {"message":"Student updated succesfully"}
    
@router.delete('/user',tags=["user"])
async def delete_user(id: str):
    result = collection_user.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        deleted_id = str(result["_id"])
        response_data = {"message": "Todo deleted successfully", "data": deleted_id}
        return JSONResponse(content=response_data, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Todo not found")
