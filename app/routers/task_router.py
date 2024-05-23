from typing import Any, List
from fastapi import APIRouter, status, Depends
from app.controllers.task_controllers import ControllerTask
from app.schemas.task_schema import MessageResponse, Task, TaskNew, TaskShow


router = APIRouter(prefix="/task", tags=["Tasks"])

def get_controller_task() -> ControllerTask:
    return ControllerTask()

@router.get("/", status_code=status.HTTP_200_OK,response_model=List[TaskShow])
async def get_all_tasks(controller_task: ControllerTask = Depends(get_controller_task)):
    ret = controller_task.get_all_tasks()
    return ret

# @router.get("/pages/{assigned_to}", status_code=status.HTTP_200_OK,response_model=List[TaskShow])
# async def get_all_tasks_pages_user(limit: int,offset: int, assigned_to: str, controller_task: ControllerTask = Depends(get_controller_task)):
#     ret = controller_task.get_all_tasks_pages_user(limit,offset,assigned_to)
#     return ret

@router.get("/{assigned_to}", status_code=status.HTTP_200_OK,response_model=List[TaskShow])
async def get_all_tasks_user(assigned_to: str, controller_task: ControllerTask = Depends(get_controller_task)):
    ret = controller_task.get_all_tasks_user(assigned_to)
    return ret


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskShow)
async def create_task(task: TaskNew, controller_task: ControllerTask = Depends(get_controller_task)):
    ret = await controller_task.create_task(task)
    return ret


@router.get("/{assigned_to}/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskShow)
async def get_task_by_id_user(assigned_to: str, task_id: int, controller_task: ControllerTask = Depends(get_controller_task)):
    ret = await controller_task.get_task_by_id_user(assigned_to, task_id)
    return ret


@router.patch("/{assigned_to}/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskShow)
async def update_task_user(assigned_to: str, task_id: int, task: TaskNew, controller_task: ControllerTask = Depends(get_controller_task)):
    ret = await controller_task.update_task_user(assigned_to, task_id, task)
    return ret


@router.delete("/{assigned_to}/{task_id}", status_code=status.HTTP_200_OK,response_model=MessageResponse)
async def delete_task_user(assigned_to: str, task_id: int, controller_task: ControllerTask = Depends(get_controller_task)):  
    ret = await controller_task.delete_task_user(assigned_to, task_id)
    return ret

