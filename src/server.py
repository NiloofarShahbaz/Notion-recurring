import uvicorn
from fastapi import FastAPI

from src.database import db
from src.recurring_event import api

app = FastAPI()
app.include_router(api.router)
db.generate_mapping(create_tables=True)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)
