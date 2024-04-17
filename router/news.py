from fastapi import APIRouter, Depends, HTTPException
import DB.crud as crud
import DB.dependencies as dependencies
import DB.schemas as schemas
from sqlalchemy.orm import Session
from typing import Union

from crawling.news import get_yesterday, crawling_news

router = APIRouter(prefix="/api/v1/news", tags=["crawling"])

# 오늘 기준 어제 날짜 가져오기
@router.get("/yesterday")
def get_day():
    yesterday = get_yesterday()
    return {'yesterday' : yesterday}

# # 오늘 기준 어제자 뉴스 크롤링
@router.post("/save")
async def crawling_it_news():
    message = await crawling_news()
    print("message:", message)
    return message

# @router.post('/', response_model=schemas.News)
# def create_news(news: schemas.NewsCreate, db: Session = Depends(dependencies.get_db)):
#     db_news = crud.create_news(db, news)
#     return db_news

@router.get("/{news_index}")
def get_news_id(news_index: int, db: Session = Depends(dependencies.get_db)):
    print(f'type: {news_index}')
    print(f'type: {type(news_index)}')

    try: 
        news_index = int(news_index)
        if isinstance(news_index, int):
            db_news = crud.get_news_id(db, news_index)
    except:     
        if isinstance(news_index, str):
            db_news = crud.get_news_title(db, index)

    if db_news is None:
        raise HTTPException(status_code=404, detail='News Not Found')
    return db_news

@router.get('/')
def get_all_news(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    return crud.get_all_news(db, skip, limit)
