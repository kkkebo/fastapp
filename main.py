from fastapi import FastAPI

from api import users, news
from db.db_setup import async_engine
from db.models import user


async def async_main():
    async with async_engine.connect() as conn:
        await conn.run_sync(user.Base.metadata.create_all)

    # async with AsyncSessionLocal() as session:
    #     yield session
    #     await session.commit()

        # for AsyncEngine created in function scope, close and
        # clean-up pooled connections
    await async_engine.dispose()


app = FastAPI(
    title="Fast API",
    description="API for ...",
    version="0.0.1",
    contact={
        "name": "VTBHack",
        "email": "VTBHack@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(users.router)
app.include_router(news.router)

