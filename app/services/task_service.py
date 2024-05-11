from app.repositories.task_i_repository import ITaskRepository
from app.repositories.task_postgresql import TaskPostgreSQLRepository
from app.repositories.repository_dependencies import session


def get_task_service() -> ITaskRepository:
    return TaskPostgreSQLRepository(session)
