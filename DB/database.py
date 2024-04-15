from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# (1) 비동기 방식 - Starlette
# (2) 데이터 검증 - pydantic

## .env 사용
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# pip install pymysql
# 동기용 데이터 베이스 설정 
SQLALCHEMY_DATABASE_URL = DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# FIXME: sqlalchemy.exc.InvalidRequestError: The asyncio extension requires an async driver to be used. The loaded 'pymysql' is not async.
# # # 비동기용 데이터 베이스 설정 -> aiomysql (pip install aiomysql)
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# ASYNC_SQLALCHEMY_DATABASE_URL = DATABASE_URL
# async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
# AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)

Base = declarative_base()