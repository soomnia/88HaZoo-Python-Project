# 모듈이 인식이 안 되면
# cmd + shift + p -> python select interpreter -> .venv 선택
from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# app 객체 생성
app = FastAPI()

# APScheduler 인스턴스 생성
scheduler  = AsyncIOScheduler()

from crawling.news import crawling_news

async def scheduledJob():
    print("스케줄러가 작업을 실행합니다.")
    await crawling_news()

scheduler.add_job(scheduledJob, 'cron', hour='09', minute='30')

scheduler.start()

# 127.0.0.1:8000/
@app.get("/")
def index():
    return {"Hello":"World"}

# router 연결
from router.news import router as news_router
app.include_router(news_router)

from router.weather import router as weather_router
app.include_router(weather_router)

# python main.py 로 실행했을 때 uvicorn 명령어로 실행시킨 것과 동일하게 하기 위함
if __name__ == "__main__":
    # ASGI 서버 실행 (비동기식)
    import uvicorn
    # main.py에서 app을 실행시켜줘
    uvicorn.run("main:app", reload=True)