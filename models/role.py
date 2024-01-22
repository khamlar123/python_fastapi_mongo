from pydantic import BaseModel
from bson import ObjectId
class Role(BaseModel):
    name: str
    url: str
    icon: str