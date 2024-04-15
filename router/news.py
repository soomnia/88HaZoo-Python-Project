from fastapi import APIRouter
from crawling.naver_it_news import get_yesterday
from crawling.web_crawling import crawling_news, save_in_db

router = APIRouter(prefix="/api/v1/news", tags=["crawling"])

# 오늘 기준 어제 날짜 가져오기
@router.get('/yesterday')
def get_day():
    yesterday = get_yesterday()
    return {'yesterday' : yesterday}

# # 오늘 기준 어제자 뉴스 크롤링
@router.post('/')
async def crawling_it_news():
    message = await crawling_news()
    print("message:", message)
    return message