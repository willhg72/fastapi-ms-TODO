from datetime import datetime
from typing import Any, List
from uuid import uuid4
from app.controllers.utils import get_task_service
from app.utilities.utility_data_task import Fake_Data_Task

data= Fake_Data_Task("fake_data_task.json")


repository = get_task_service()

class ControllerTask:

    async def get_all_tasks(self, page: int, offset: int) -> dict:
        self.fake_tasks = await data.get_fake_data_task()
        segment: dict[str,int] = self.pagination(page, offset)
        list_response = list(self.fake_tasks)
        list_response = list_response[segment["start"] - 1 : segment["end"]]
        return {"total_items" : segment['total'],
                "response": list_response
                }

    async def new_task(self):
        pass 

    async def get_task(self):
        pass

    async def update_task(self):
        pass

    async def delete_task(self):
        pass

    def pagination(self, page: int, offset: int):
        if page == 1 or page == 0:
            start = 1
            end = offset
        if page > 1:
            start = (page -1) * offset
            end = page * offset

        return {
            'start': start ,
            'end': end,
            'total': len(self.fake_tasks)
        }
