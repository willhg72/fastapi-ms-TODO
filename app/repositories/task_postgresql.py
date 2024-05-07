from typing import Any
from app.repositories.task_i_repository import TaskIRepository
from app.schemas.task_schema import TaskShow


class TaskPostgreSQLRepository(TaskIRepository):
    async def __init__(self, connection_postgres):
        super().__init__()
        self.connection_postgres = connection_postgres

    @classmethod
    async def get_all_tasks(self, page: int, offset: int):
        pass

    @classmethod
    async def get_task_by_id(self, task_id: int):
        pass

    @classmethod
    async def create_task(self, task: TaskShow):
        pass

    @classmethod
    async def update_task(self, task_id: int):
        pass

    @classmethod
    async def delete_task(self, task_id: int):
        pass
