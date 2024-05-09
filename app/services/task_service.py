from app.models.task_model import Task
from app.repositories.task_i_repository import ITaskRepository
from app.schemas.task_schema import TaskShow


class TaskService:

    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    async def get_all_tasks(self, page: int, offset: int) -> list[TaskShow]:
        raise NotImplementedError

    async def get_task_by_id(self, task_id: int) -> TaskShow:
        raise NotImplementedError

    async def create_task(self, task: Task) -> TaskShow:
        raise NotImplementedError

    async def update_task(self, task_id: int) -> None:
        raise NotImplementedError

    async def delete_task(self, task_id: int) -> None:
        raise NotImplementedError
