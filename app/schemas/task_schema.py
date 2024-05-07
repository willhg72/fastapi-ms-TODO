from datetime import datetime
from pydantic import BaseModel, UUID4

from app.schemas.task_enums import StatusTask


class Task(BaseModel):
    id: int
    title: str
    description: str
    assigned_to: UUID4
    status: StatusTask
    completed: bool
    due_date: datetime
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Learn FastAPI",
                "description": "Learn FastAPI from scratch",
                "assigned_to" : "123e4567-e89b-12d3-a456-426614174000",
                "completed": False,
                "status": "pending",
                "due_date": "2023-04-20"
            }
        }


class TaskShow(BaseModel):
    id: int
    title: str
    description: str
    assigned_to: UUID4
    status: StatusTask
    due_date: datetime

    class config():
        from_attributes = True

