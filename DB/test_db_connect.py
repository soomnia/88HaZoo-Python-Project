from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

## .env 사용
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# print("*" * 20)
# print(DATABASE_URL)
# print("*" * 20)

try:
    # 엔진 생성
    engine = create_engine(DATABASE_URL)
    # 세션 생성
    SessionLocal = sessionmaker(bind=engine)

    # 세션으로 DB 연결
    session = SessionLocal()
    # 이후 세션 종료
    session.close()

    print("연결 이상 없음!")
except OperationalError as e:
    print("연결 이상 있음!")
    print(e)
