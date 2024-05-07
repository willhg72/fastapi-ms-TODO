import json
import os


current_dir = os.getcwd()


class Fake_Data_Task:
    def __init__(self, file: str):
        self.file = file

    async def get_fake_data_task(self):
        with open(f"{current_dir}\\app\\{self.file}") as f:
            data = json.load(f)

        return (data)
