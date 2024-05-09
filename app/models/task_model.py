from sqlalchemy import Column, DateTime, Integer, String, UUID, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from app.repositories.repository_dependencies import *

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    assigned_to = Column(UUID)
    completed = Column(Boolean)
    due_date = Column(DateTime(timezone=True))
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())

