from app.repositories.task_postgresql import TaskPostgreSQLRepository
from app.services.task_service import TaskService


def get_task_service() -> TaskService:
    return TaskService(TaskPostgreSQLRepository())
