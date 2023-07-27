import os

DATABASE_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("POSTGRES_HOST", "localhost"),
                "port": os.getenv("POSTGRES_PORT", "5432"),
                "user": os.getenv("POSTGRES_USER", "postgres"),
                "password": os.getenv("POSTGRES_PASSWORD", "postgres"),
                "database": os.getenv("POSTGRES_DB", "notion_recurring"),
            },
        }
    },
    "apps": {"recurring_event": {"models": ["src.recurring_event.models"]}},
    "use_tz": False,
    "timezone": "UTC",
}
