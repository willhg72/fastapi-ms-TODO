from datetime import datetime
from pydantic import BaseModel, UUID4, Field

from app.schemas.task_enums import StatusTask


class Task(BaseModel):
    id: int = Field(examples=[1])
    title: str = Field(examples=["Learn FastAPI"])
    description: str = Field(examples=["Learn FastAPI from scratch"])
    assigned_to: UUID4 = Field(examples=["123e4567-e89b-12d3-a456-426614174000"])
    status: StatusTask = Field(examples=["PENDING"])
    completed: bool = Field(examples=[False])
    due_date: datetime = Field(examples=["2023-04-20T15:39:59.133Z"])
    create_at: datetime = Field(examples=["2023-04-20T15:39:59.133Z"])
    update_at: datetime = Field(examples=["2023-04-20T15:39:59.133Z"])

    class Config:
        from_attributes = True


class TaskShow(BaseModel):
    id: int = Field(examples=[1])
    title: str = Field(examples=["Learn FastAPI"])
    description: str = Field(examples=["Learn FastAPI from scratch"])
    assigned_to: UUID4 = Field(examples=["123e4567-e89b-12d3-a456-426614174000"])
    status: StatusTask = Field(examples=["PENDING"])
    due_date: datetime = Field(examples=["2023-04-20T15:39:59.133Z"])

    class config():
        from_attributes = True
