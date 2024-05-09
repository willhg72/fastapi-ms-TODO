import os
from typing import Any
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv('app.env')


engine = create_engine(os.environ["DATABASE_URL"])
print(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


########################################


# from contextlib import asynccontextmanager
# from dataclasses import dataclass
# from typing import Optional, AsyncGenerator

# from sqlalchemy import create_engine, pool
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session, scoped_session

# Base = declarative_base()


# class SingletonDBManager(type):
#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]


# class DataBaseError(Exception):
#     pass


# @dataclass
# class DataBaseManager(metaclass=SingletonDBManager):
#     DATABASE_USERNAME: Optional[str] = config("DATABASE_USERNAME")
#     DATABASE_PASSWORD: Optional[str] = config("DATABASE_PASSWORD")
#     DATABASE_URI: Optional[str] = config("DATABASE_URI")
#     DATABASE_PORT: Optional[str] = config("DATABASE_PORT", cast=int)
#     DATABASE_NAME: Optional[str] = config("DATABASE_NAME")
#     POOL_SIZE: int = 20
#     MAX_OVERFLOW: int = 5
#     POOL_RECYCLE: int = 60

#     def __init__(self):
#         self._engine = None
#         self._sync_engine = None
#         self._async_engine = None

#     def __enter__(self):
#         self._session = self.session()
#         return self._session

#     async def __aenter__(self):
#         self._async_session = await self.async_session()
#         return self._async_session

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self._session.close()

#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         await self._async_session.close()

#     def sync_engine(self):
#         try:
#             if self._engine is None:
#                 self._engine = create_engine(
#                     f"postgresql+psycopg2://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_URI}:"
#                     f"{self.DATABASE_PORT}/{self.DATABASE_NAME}",
#                     pool_size=self.POOL_SIZE,
#                     max_overflow=self.MAX_OVERFLOW,
#                     pool_recycle=self.POOL_RECYCLE,
#                     pool_timeout=10,
#                 )
#             return self._engine
#         except Exception as e:
#             raise DataBaseError(f"Error creating sync engine: {e}") from e

#     async def async_engine(self):
#         try:
#             if self._async_engine is None:
#                 self._async_engine = create_async_engine(
#                     f"postgresql+asyncpg://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_URI}:"
#                     f"{self.DATABASE_PORT}/{self.DATABASE_NAME}",
#                     future=True,
#                     pool_size=self.POOL_SIZE,
#                     max_overflow=self.MAX_OVERFLOW,
#                     pool_recycle=self.POOL_RECYCLE,
#                     pool_timeout=10,
#                     pool_pre_ping=True,
#                 )
#             return self._async_engine
#         except Exception as e:
#             raise DataBaseError(f"Error creating async engine: {e}") from e

#     def session(self):
#         return sessionmaker(
#             autocommit=False,
#             autoflush=False,
#             expire_on_commit=False,
#             bind=self.sync_engine(),
#         )()

#     async def async_session(self):
#         return scoped_session(
#             sessionmaker(
#                 bind=await self.async_engine(),
#                 class_=AsyncSession,
#                 expire_on_commit=False,
#                 autoflush=False,
#                 autocommit=False,
#             )
#         )()


# db_manager = DataBaseManager()


# @asynccontextmanager
# async def get_async_session():
#     db = await db_manager.async_session()
#     try:
#         yield db
#     finally:
#         await db.close()


# async def get_db() -> AsyncGenerator[AsyncSession, None]:
#     async with get_async_session() as db:
#         yield db
