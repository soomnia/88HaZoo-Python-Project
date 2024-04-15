from models import News
from schemas import NewsCreate, NewsUpdate
from sqlalchemy.orm import Session

    # ## 제목, 언론사, 작성일, 링크, 전체 내용
    # id = Column(Integer, primary_key=True, index=True)
    # category = Column(String)
    # title = Column(String)
    # press = Column(String)
    # date = Column(String)
    # link = Column(String)
    # content = Column(Text)


    # CREATE TABLE fast_api_test.news (
    #      id INT AUTO_INCREMENT PRIMARY KEY,
    #      category VARCHAR(15),
    #      title VARCHAR(255),
    #      press VARCHAR(15),
    #      date VARCHAR(30),
    #      link VARCHAR(255),
    #      content Text
    # );

# create news
def create_news(db: Session, news: NewsCreate):
    db_news = News(category=news.category, title=news.title, press=news.press, date = news.date, link=news.link, content=news.content)
    db.add(db_news)
    db.commit()
    return db_news

def get_news_id(db: Session, news_id: int):
    return db.query(News).filter(News.id == news_id).first()

def get_news_title(db: Session, news_title):
    return db.query(News).filter(News.title == news_title).first()

# 전체 조회 (페이지 네이션)
def get_all_news(db: Session, skip: int=0, limit: int = 10):
    return db.query(News).offset(skip).limit(limit).all()
