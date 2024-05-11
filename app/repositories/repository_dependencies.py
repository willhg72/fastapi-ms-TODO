from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

from app.utilities.utility_data_task import DATABASE_URL

engine = create_engine(DATABASE_URL)
session = Session(engine)

class Base(DeclarativeBase):
    pass
