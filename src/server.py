import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.recurring_event import api
from src.settings import DATABASE_CONFIG

app = FastAPI()
app.include_router(api.router)
register_tortoise(app=app, config=DATABASE_CONFIG)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
