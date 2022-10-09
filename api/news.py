import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db
from pydantic_schemas.news import News, NewsCreate
from api.utils.news import get_news, get_new, create_news

router = fastapi.APIRouter()


@router.get("/news/{news_id}", response_model=News)
async def read_new(news_id: int, db: AsyncSession = Depends(async_get_db)):
    db_user = await get_new(db=db, news_id=news_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_user


@router.get("/news", response_model=list[News])
async def read_news(db: AsyncSession = Depends(async_get_db)):
    db_users = await get_news(db)
    return db_users


@router.post("/news", response_model=News, status_code=201)
async def create_new_news(news: NewsCreate, db: AsyncSession = Depends(async_get_db)):
    db_user = await create_news(db=db, news=news)
    return db_user

