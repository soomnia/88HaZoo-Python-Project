from pydantic import BaseModel
from typing import List

    # id = Column(Integer, primary_key=True, index=True)
    # category = Column(String)
    # title = Column(String)
    # press = Column(String)
    # date = Column(String)
    # link = Column(String)
    # content = Column(String)

class NewsBase(BaseModel):
    category: str
    title: str
    press: str
    date: str
    link: str
    content: str

class NewsCreate(NewsBase):
    pass

class NewsUpdate(NewsBase):
    title: str | None = None
    link: str | None = None

## 데이터베이스에서 아이템을 읽을 때 사용됩니다.
# 이 클래스는 NewsBase 확장하고, 데이터베이스에서 생성된 ID와 같은 추가적인 정보를 포함합니다.
class News(NewsBase):
    id: int
    items: List[NewsBase]

    class Config:
        orm_mode = True
