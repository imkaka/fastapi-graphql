from orator import DatabaseManager, Schema, Model

from .config import settings

DATABASES = {
    "postgres": {
        "driver": settings.POSTGRES_DRIVER,
        "host": settings.POSTGRES_SERVER,
        "database": settings.POSTGRES_DB,
        "user": settings.POSTGRES_USER,
        "password": settings.POSTGRES_PASSWORD,
        "prefix": "",
        "port": settings.POSTGRES_PORT,
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
