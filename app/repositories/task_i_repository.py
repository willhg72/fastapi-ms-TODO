from abc import ABC

from app.schemas.task_schema import TaskShow

class TaskIRepository(ABC):

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
