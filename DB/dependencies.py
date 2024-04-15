from DB.database import SessionLocal
# from DB.database import AsyncSessionLocal

# 동기용 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # 비동기용 의존성
# async def get_async_db():
#     async with AsyncSessionLocal() as session:
#         yield session