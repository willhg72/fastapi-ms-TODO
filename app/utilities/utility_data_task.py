import json
import os
from dotenv import load_dotenv


current_dir = os.getcwd()

load_dotenv("app/.env")
DATABASE_URL = f'{os.environ["DB_DRIVER"]}://{os.environ["DB_USER"]}:{os.environ["DB_PASS"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}'


class Fake_Data_Task:
    def __init__(self, file: str):
        self.file = file

    async def get_fake_data_task(self):
        with open(f"{current_dir}\\app\\{self.file}") as f:
            data = json.load(f)

        return (data)


