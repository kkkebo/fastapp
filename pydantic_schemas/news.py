from pydantic import BaseModel
from datetime import datetime

class NewsBase(BaseModel):
    title: str
    news_url: str
    category: str
    feature_0: str
    feature_1: str



class NewsCreate(NewsBase):
    ...


class News(NewsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
