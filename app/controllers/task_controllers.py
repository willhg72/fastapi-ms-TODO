from fastapi import Depends
from app.repositories.task_i_repository import ITaskRepository
from app.repositories.task_postgresql import TaskPostgreSQLRepository
from app.services.task_service import get_task_service
from app.utilities.utility_data_task import Fake_Data_Task


class ControllerTask:
    def __init__(self):
        super().__init__()

    def get_all_tasks(self, limit: int, offset: int):
        tasks = get_task_service()
        return tasks.get_all_tasks(limit, offset)

    async def new_task(self):
        pass 

    async def get_task(self):
        pass

    async def update_task(self):
        pass

    async def delete_task(self):
        pass
