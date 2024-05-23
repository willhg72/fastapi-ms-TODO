from abc import ABC, abstractmethod
from typing import Any

from app.models.task_model import Task
from app.schemas.task_schema import TaskNew, TaskShow


class ITaskRepository(ABC):

    @abstractmethod
    def get_all_tasks(self) -> list[Task]:
        raise NotImplementedError
    
    # @abstractmethod
    # def get_all_tasks_pages_user(self, page: int, offset: int, assigned_to: str) -> list[Task]:
    #     raise NotImplementedError

    @abstractmethod
    def get_all_tasks_user(self, assigned_to: str) -> list[Task]:
        raise NotImplementedError
    
    @abstractmethod
    def get_task_by_id_user(self, assigned_to: str, task_id: int) -> TaskShow:
        raise NotImplementedError

    @abstractmethod
    def create_task(self, task: TaskNew) -> TaskShow:
        raise NotImplementedError

    @abstractmethod
    def update_task_user(self, assigned_to: str, task_id: int,task: TaskNew) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_task_user(self, assigned_to: str, task_id: int) -> dict[str, str]:
        raise NotImplementedError
