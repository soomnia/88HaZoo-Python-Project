# DB Connection

from DB.database import Base
from sqlalchemy import Column, Integer, String, Text

class News(Base):
    __tablename__ = 'news'

    ## 제목, 언론사, 작성일, 링크, 전체 내용
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    title = Column(String)
    press = Column(String)
    date = Column(String)
    link = Column(String)
    content = Column(Text)
