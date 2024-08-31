from .db_config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

TORTOISE_CONFIG = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': DB_HOST,
                'port': DB_PORT,
                'user': DB_USER,
                'password': DB_PASS,
                'database': DB_NAME,
            }
        },
    },
    "apps": {
        "models": {
            "models": ["database.models", "aerich.models"],
            "default_connection": "default"
        }
    }
} 
