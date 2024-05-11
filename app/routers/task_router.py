from typing import List
from fastapi import APIRouter, status, Depends
from app.controllers.task_controllers import ControllerTask
from app.schemas.task_schema import TaskShow


router = APIRouter(prefix="/task", tags=["Tasks"])

def get_controller_task() -> ControllerTask:
    return ControllerTask()


@router.get("/", response_model=List[TaskShow])
async def get_all_tasks(
    limit: int,
    offset: int,
    controller_task: ControllerTask = Depends(get_controller_task)
):
    ret = controller_task.get_all_tasks(limit,offset)
    return ret


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskShow)
async def new_task(task: TaskShow):
    pass


@router.get("/{task_id}")
async def get_task(task_id: int):
    pass


@router.patch("/{task_id}")
async def update_task(task: TaskShow):
    pass


@router.delete("/{task_id}")
async def delete_task(task_id: int):
    pass
