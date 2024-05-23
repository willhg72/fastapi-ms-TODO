from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, Field
from pydantic.functional_validators import AfterValidator
from app.schemas.task_enums import StatusTask

def check_str_length(v):
    if isinstance(v, str):
        assert len(v) >= 10, "The field must be a valid user id"
    return v


userIdValid = Annotated[str, AfterValidator(check_str_length)]



class Task(BaseModel):
    id: int = Field(examples=[1])
    title: str = Field(examples=["Learn FastAPI"])
    description: str = Field(examples=["Learn FastAPI from scratch"])
    assigned_to: userIdValid = Field(...,examples=["wduu2bks8dzbjvt"],)
    status: StatusTask = Field(examples=["pending"])
    completed: bool = Field(examples=[False])
    due_date: datetime = Field(examples=["2023-04-20T15:39:59.133Z"])
    create_at: datetime  | None = Field(examples=["2023-04-20T15:39:59.133Z"])
    update_at: datetime | None = Field(examples=["2023-04-20T15:39:59.133Z"])

    class Config:
        from_attributes = True


class TaskShow(BaseModel):
    id: int = Field(examples=[1])
    title: str = Field(examples=["Learn FastAPI"])
    description: str = Field(examples=["Learn FastAPI from scratch"])
    assigned_to: userIdValid = Field(...,examples=["wduu2bks8dzbjvt"])
    completed: bool = Field(examples=[False])
    status: StatusTask = Field(examples=["pending"])
    due_date: datetime = Field(examples=["2024-05-23"])

    class config():
        from_attributes = True
        
class TaskNew(BaseModel):   
    title: str = Field(examples=["Learn FastAPI"])
    description: str = Field(examples=["Learn FastAPI from scratch"])
    assigned_to: userIdValid = Field(...,examples=["wduu2bks8dzbjvt"])
    completed: bool = Field(examples=[False])
    status: StatusTask = Field(examples=["pending"])
    due_date: datetime = Field(examples=["2024-06-20"])
    
    class config():
        from_attributes = True
        
        
class MessageResponse(BaseModel):
    message: str = Field(examples=["Task deleted"]) 
    
class TaskAuth(BaseModel):
    token: str = Field(examples=["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"])
    assigned_to: userIdValid = Field(examples=["wduu2bks8dzbjvt"])