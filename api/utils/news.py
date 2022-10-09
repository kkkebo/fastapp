from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from db.models.user import News
from pydantic_schemas.news import NewsCreate


async def get_new(db: AsyncSession, news_id: int) -> News | None:
    query = select(News).where(News.id == news_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_news(db: AsyncSession) -> list[News]:
    query = select(News)
    result = await db.execute(query)
    return result.scalars().all()


async def create_news(db: AsyncSession, news: NewsCreate) -> News:
    db_user = News(**news.dict())
    db.add(db_user)
    await db.commit()
    return db_user
