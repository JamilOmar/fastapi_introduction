


from typing import Annotated
from db.dependencies import get_db
from db import SessionLocal
from .todo import TodoRepository
from fastapi import Depends

def get_todo_repository( session: Annotated[SessionLocal, Depends(get_db)]):
    return TodoRepository(session) 
