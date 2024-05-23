from fastapi import HTTPException
from app.repositories.repository_dependencies import *
from app.repositories.task_i_repository import ITaskRepository
from app.models.task_model import Task
from app.schemas.task_schema import TaskNew, TaskShow


class TaskPostgreSQLRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def get_all_tasks(self) -> list[Task]:
        tasks = self.db.query(Task).all()
        return tasks

    # def get_all_tasks_pages_user(self, limit: int, offset: int, assigned_to: str) -> list[Task]:
    #     tasks = self.db.query(Task).offset(offset).limit(limit).filter(Task.assigned_to == assigned_to).all()
    #     return tasks

    def get_all_tasks_user(self, assigned_to: str) -> list[Task]:
        tasks = self.db.query(Task).filter(Task.assigned_to == assigned_to).all()
        return tasks


    def get_task_by_id_user(self, assigned_to: str, task_id: int) -> TaskShow:
        task = self.db.query(Task).filter(Task.assigned_to == assigned_to).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return TaskShow(**task.__dump__())
        

    def create_task(self, task: TaskNew):
        # return task
        new_task = Task(**task.model_dump())
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        self.db.close()
        return new_task




    def update_task_user(self, assigned_to: str, task_id: int, task: TaskNew):
        task_update = self.db.query(Task).filter(Task.id == task_id).filter(Task.assigned_to == assigned_to).first()
        if task_update is None:
            raise HTTPException(status_code=404, detail="Task not found")
        task_update.__update__(**task.model_dump(exclude_unset=True))
        self.db.add(task_update)
        self.db.commit()
        self.db.refresh(task_update)
        self.db.close()
        return task_update
        
        


    def delete_task_user(self, assigned_to: str, task_id: int) -> dict[str, str]:
        task = self.db.query(Task).filter(Task.id == task_id).filter(Task.assigned_to == assigned_to).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        self.db.delete(task)
        self.db.commit()
        self.db.close()
        return {"message": "Task deleted"}
