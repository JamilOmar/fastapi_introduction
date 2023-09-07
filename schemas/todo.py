from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    content: str

    
class Todo(TodoBase):
    class Config:
        orm_mode = True
    
    
class TodoInfo(TodoBase):
    id: int
    date_created: datetime
    class Config:
        orm_mode = True
