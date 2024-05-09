from typing import Any

from fastapi import Depends
from app.repositories.repository_dependencies import SessionLocal, get_db
from app.repositories.task_i_repository import ITaskRepository
from app.models.task_model import Task
from sqlalchemy.orm import Session


class TaskPostgreSQLRepository(ITaskRepository):
    async def __init__(self):
        super().__init__()
        self.db: Session = SessionLocal()

    async def get_all_tasks(self, page: int, offset: int, db: Session = Depends(get_db)) -> list[Task]:
        raise NotImplementedError

    async def get_task_by_id(self, task_id: int, db: Session = Depends(get_db)) -> Task:
        raise NotImplementedError

    async def create_task(self, task: Task, db: Session = Depends(get_db)) -> Task:
        raise NotImplementedError

    async def update_task(self, task_id: int, db: Session = Depends(get_db)) -> None:
        raise NotImplementedError

    async def delete_task(self, task_id: int, db: Session = Depends(get_db)) -> None:
        raise NotImplementedError
