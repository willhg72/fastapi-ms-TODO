from app.repositories.repository_dependencies import *
from app.repositories.task_i_repository import ITaskRepository
from app.models.task_model import Task


class TaskPostgreSQLRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all_tasks(self, limit: int, offset: int) -> list[Task]:
        tasks = self.db.query(Task).offset(offset).limit(limit).all()
        return tasks

    def task_by_id(self, task_id: int) -> Task:
        raise NotImplementedError

    def create_task(self, task: Task) -> Task:
        raise NotImplementedError

    def update_task(self, task_id: int) -> None:
        raise NotImplementedError

    def delete_task(self, task_id: int) -> None:
        raise NotImplementedError
