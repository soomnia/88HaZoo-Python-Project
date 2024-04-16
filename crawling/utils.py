
import asyncio
import pandas as pd

from DB.database import SessionLocal
import csv
from DB.models import News

async def save_csv_file(df: pd.DataFrame, file_name: str):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, df.to_csv, file_name)


async def insert_news_file(file_name: str):
    db = SessionLocal()
    try:
        # CSV 파일 내용을 읽어서 데이터베이스에 저장
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            ## 첫 번째 줄을 건너 뛰기! (칼럼 명)
            next(csv_reader) 
            for row in csv_reader:
                print("data:", row)
                item = News(category=row[1],
                            title=row[2],
                            press=row[3],
                            date=row[4],
                            link=row[5],
                            content=row[6])
                db.add(item)
                db.commit()
    except Exception as e:
        db.rollback()
        return {"error": f"insert_news_file - {str(e)}"}
    finally:
        db.close()