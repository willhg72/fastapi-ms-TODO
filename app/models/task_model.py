# from datetime import datetime
# from typing import Annotated
# from sqlalchemy import Column, DateTime, Integer, String, UUID, Boolean
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.sql import func
# from app.repositories.repository_dependencies import *


# intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
# timestamp = Annotated[
#     datetime,
#     mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
# ]


# class Task(Base):
#     __tablename__ = "tasks"
#     id = mapped_column(Integer, primary_key=True, index=True)
#     title = Column(String(255))
#     description = Column(String(255))
#     assigned_to = Column(UUID, nullable=True)
#     completed = Column(Boolean)
#     due_date = Column(DateTime(timezone=True), nullable=True)
#     create_at = Column(DateTime(timezone=True), server_default=func.now())
#     update_at = Column(DateTime(timezone=True), onupdate=func.now())


from datetime import datetime
from typing import Annotated
from sqlalchemy import DateTime, Integer, String,  Boolean
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func
from app.repositories.repository_dependencies import *
from app.schemas.task_enums import StatusTask


intpk = Annotated[int, mapped_column(primary_key=True, index=True, autoincrement=True)]
timestamp = Annotated[
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    title = mapped_column(String(255))
    description = mapped_column(String(255))
    assigned_to = mapped_column(String(100), nullable=False)
    completed = mapped_column(Boolean, default=False)
    status: Mapped[StatusTask]
    due_date = mapped_column(DateTime(timezone=True), nullable=True)
    create_at : Mapped[timestamp]
    update_at : Mapped[timestamp]
    
    def __dump__(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "assigned_to": self.assigned_to,
            "completed": self.completed,
            "status": self.status.value,
            "due_date": self.due_date,
            "create_at": self.create_at,
            "update_at": self.update_at,
        }
        
    def __update__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self
