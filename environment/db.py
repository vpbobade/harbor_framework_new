import os
from sqlalchemy import create_engine

DB_HOST = os.getenv("DB_HOST", "wrong-host")
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "appdb"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def get_db():
    conn = engine.connect()
    return conn
