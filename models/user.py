from pydantic import BaseModel

class Users(BaseModel):
    userName: str
    name: str
    password: str
    status: int
    