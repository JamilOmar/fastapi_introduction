# apps.members.models

from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from db.base import Base
class Todo(Base):
    
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True)
    content = Column(String(200) , nullable=False)
    date_created = Column(DateTime,default = datetime.utcnow)
    
    def __repr__(self) -> str:
        return '<Task {}>'.format(self.id)