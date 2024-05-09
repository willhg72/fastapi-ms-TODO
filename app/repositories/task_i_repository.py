from abc import ABC, abstractmethod

from app.models.task_model import Task

class ITaskRepository(ABC):

    @abstractmethod
    async def get_all_tasks(self, page: int, offset: int) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    async def get_task_by_id(self, task_id: int) -> Task:
        raise NotImplementedError

    @abstractmethod
    async def create_task(self, task: Task) -> Task:
        raise NotImplementedError

    @abstractmethod
    async def update_task(self, task_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_task(self, task_id: int) -> None:
        raise NotImplementedError
