from fastapi import APIRouter

from app.controllers.task_controllers import ControllerTask
from app.schemas.task_schema import TaskShow

router = APIRouter(prefix="/task", tags=["Tasks"])
controller_task = ControllerTask()

@router.get("/")
async def get_all_tasks(page: int = 1, offset: int = 10):
    ret = await controller_task.get_all_tasks(page, offset)
    return ret


@router.post("/")
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
