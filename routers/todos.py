from typing import Annotated, List
from fastapi import APIRouter, Depends,HTTPException
from schemas import TodoInfo ,Todo
from repositories import get_todo_repository
from repositories.todo import TodoRepository

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.get("/",response_model=List[TodoInfo])
async def get_todos(todo_service:Annotated[TodoRepository, Depends(get_todo_repository)]):
    return await todo_service.get_all()

@router.get("/{id}",response_model=TodoInfo)
async def get_by_id(id:int,todo_service:Annotated[TodoRepository, Depends(get_todo_repository)]):
    todo = await todo_service.get_by_id(id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/")
async def create_todos(todo: Todo , todo_service:Annotated[TodoRepository, Depends(get_todo_repository)]):
    await todo_service.create(todo)
    
@router.delete("/{id}")
async def delete_item(id:int , todo_service:Annotated[TodoRepository, Depends(get_todo_repository)]):
    await todo_service.delete(id)
    
@router.patch("/{id}")
async def update_item(id:int,todo: Todo , todo_service:Annotated[TodoRepository, Depends(get_todo_repository)]):
    await todo_service.update(id,todo)


