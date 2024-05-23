from fastapi import Depends
from app.repositories.task_i_repository import ITaskRepository
from app.repositories.task_postgresql import TaskPostgreSQLRepository
from app.services.task_service import get_task_service
from app.utilities.utility_data_task import Fake_Data_Task


class ControllerTask:
    def __init__(self):
        self.task_service = get_task_service()

    def get_all_tasks(self):
        return self.task_service.get_all_tasks()

    # def get_all_tasks_pages_user(self, limit: int, offset: int, assigned_to: str):
    #     return self.task_service.get_all_tasks_pages_user(limit, offset, assigned_to)

    def get_all_tasks_user(self, assigned_to: str):
        return self.task_service.get_all_tasks_user(assigned_to)



    async def create_task(self, task):
        return self.task_service.create_task(task)



    async def get_task_by_id_user(self, assigned_to: str, id: int):
        return self.task_service.get_task_by_id_user(assigned_to, id)
        


    async def update_task_user(self, assigned_to: str, task_id: int, task):
        return self.task_service.update_task_user(assigned_to,task_id,task)



    async def delete_task_user(self, assigned_to: str, task_id: int):
        return self.task_service.delete_task_user(assigned_to, task_id)
        
