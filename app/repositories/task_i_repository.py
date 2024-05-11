from abc import ABC, abstractmethod

from app.models.task_model import Task


class ITaskRepository(ABC):

    @abstractmethod
    def get_all_tasks(self, page: int, offset: int) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    def task_by_id(self, task_id: int) -> Task:
        raise NotImplementedError

    @abstractmethod
    def create_task(self, task: Task) -> Task:
        raise NotImplementedError

    @abstractmethod
    def update_task(self, task_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        raise NotImplementedError
