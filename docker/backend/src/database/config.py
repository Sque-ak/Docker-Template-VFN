from src.settings import settings


TORTOISE_ORM = {
    "connections": 
     {"default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "database": settings.POSTGRESQL_DATABASE,
                    "host": settings.POSTGRESQL_HOSTNAME_DOCKER,
                    "password": settings.POSTGRESQL_PASSWORD,
                    "user": settings.POSTGRESQL_USERNAME,
                    "port": 5432
                }
            },
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "src.database.models", 
            ],
            "default_connection": "default"
        }
    }
}
