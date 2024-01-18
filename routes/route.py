from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from config.database import collection_name, collection_user
from models.todo import Todo
from models.user import Users
from schemas.todo import list_serial
from schemas.user import list_users
from bson import ObjectId
router = APIRouter()

@router.get('/todo', tags=["todo"])
async def get_todos():
    todos = list_serial(collection_name.find())
    response_data = {"message": "get Todo successfully", "data": todos}
    return JSONResponse(content=response_data, status_code=201)

@router.post('/todo', tags=["todo"])
async def post_todos(todo: Todo):
    result = collection_name.insert_one(dict(todo))
    inserted_id = result.inserted_id
    # Create a custom response with the resource ID
    response_data = {"message": "Todo created successfully", "data": str(inserted_id)}
    # Return the custom JSON response
    return JSONResponse(content=response_data, status_code=201)
   
@router.put('/todo', tags=["todo"])
async def put_todos(id: str,todo: Todo):
    result =  collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)}, return_document=True )
    if result:
        updated_id = str(result["_id"])
        response_data = {"message": "Todo updated successfully", "data": updated_id}
        return JSONResponse(content=response_data, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Todo not found")

@router.delete('/todo',tags=["todo"])
async def delete_todos(id: str):
    result = collection_name.find_one_and_delete({"_id": ObjectId(id)})

    if result:
        deleted_id = str(result["_id"])
        response_data = {"message": "Todo deleted successfully", "data": deleted_id}
        return JSONResponse(content=response_data, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Todo not found")
    
@router.get('/user',tags=["user"])
async def get_user():
    users = list_users(collection_user.find())
    response_data = {"message": "get user successfully", "data": users}
    return JSONResponse(content=response_data, status_code=201)

@router.post('/user', tags=["user"])
async def post_users(user: Users):
    result = collection_user.insert_one(dict(user))
    inserted_id = result.inserted_id
    response_data = {"message": "Todo created successfully", "data": str(inserted_id)}
    return JSONResponse(content=response_data, status_code=201)

@router.put('/user', tags=["user"])
async def put_todos(id: str,user: Users):
    result =  collection_user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)}, return_document=True )
    if result:
        updated_id = str(result["_id"])
        response_data = {"message": "Todo updated successfully", "data": updated_id}
        return JSONResponse(content=response_data, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Todo not found")
    
