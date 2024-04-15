# 모듈이 인식이 안 되면
# cmd + shift + p -> python select interpreter -> .venv 선택
from fastapi import FastAPI

# app 객체 생성
app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
def index():
    return {"Hello":"World"}

# router 연결
from router.news import router as news_router
app.include_router(news_router)

# from router.db import router as db_router
# app.include_router(db_router)

# python main.py 로 실행했을 때 uvicorn 명령어로 실행시킨 것과 동일하게 하기 위함
if __name__ == "__main__":
    # ASGI 서버 실행 (비동기식)
    import uvicorn
    # main.py에서 app을 실행시켜줘
    uvicorn.run("main:app", reload=True)