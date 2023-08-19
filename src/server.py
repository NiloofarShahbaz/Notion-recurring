import uvicorn
from fastapi import FastAPI
from pony import orm

from src.recurring_event import api
from src.settings import DATABASE_CONFIG

app = FastAPI()
app.include_router(api.router)
db = orm.Database()
db.bind(provider="postgres", **DATABASE_CONFIG["credentials"])
db.generate_mapping(create_tables=True)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)
