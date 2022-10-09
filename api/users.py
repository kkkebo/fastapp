import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db
from pydantic_schemas.user import UserCreate, User
from api.utils.users import get_user, get_users, create_user

router = fastapi.APIRouter()


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users", response_model=list[User])
async def read_users(db: AsyncSession = Depends(async_get_db)):
    db_users = await get_users(db)
    return db_users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(async_get_db)):
    db_user = await create_user(db=db, user=user)
    return db_user

