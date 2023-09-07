
from sqlalchemy import select
from models.todo import Todo 
from schemas.todo import Todo as TodoSchema
from sqlalchemy.ext.asyncio import AsyncSession

class TodoRepository:

    def __init__(self ,session: AsyncSession) -> None:
        self.session = session

    async def create(self, todo:TodoSchema):
        new_todo =  Todo(content=todo.content)
        try:
            self.session.add(new_todo)
            await self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
    async def get_all(self)->list[Todo]:
        todos = await self.session.execute(select(Todo).order_by(Todo.date_created))
        return todos.scalars().all()
    
    async def get_by_id(self,id)->Todo:
        todo = await self.session.get(Todo,id)
        return todo
    
    async def delete(self, id):
        try:
            todo = await self.session.get(Todo,id)
            await self.session.delete(todo)
            await self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    async def update(self, id, todo:TodoSchema):
        try:
            current_todo = await self.session.get(Todo,id)
            current_todo.content = todo.content
            await self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


