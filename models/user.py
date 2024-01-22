from pydantic import BaseModel, Field
from models.role import Role

class Users(BaseModel):
    userName: str
    name: str
    password: str
    status: int
    roles: list[Role]
     