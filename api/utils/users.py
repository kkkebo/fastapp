from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from db.models.user import User
from pydantic_schemas.user import UserCreate


async def get_user(db: AsyncSession, user_id: int) -> User | None:
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_users(db: AsyncSession) -> list[User]:
    query = select(User)
    result = await db.execute(query)
    return result.scalars().all()


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    return db_user
