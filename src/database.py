from pony import orm

from src.settings import DATABASE_CONFIG

db = orm.Database()
db.bind(provider="postgres", **DATABASE_CONFIG["credentials"])
