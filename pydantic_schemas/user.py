from pydantic import BaseModel


class UserBase(BaseModel):
    age: int
    category: str
    gender: str


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
