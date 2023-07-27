from tortoise import Tortoise, run_async

from src.settings import DATABASE_CONFIG


async def init():
    await Tortoise.init(config=DATABASE_CONFIG)
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(init())
