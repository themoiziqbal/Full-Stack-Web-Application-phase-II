from sqlmodel import create_engine, Session, SQLModel
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    class Config:
        env_file = ".env"

settings = Settings()

engine = create_engine(settings.database_url, echo=True)

def init_db():
    # In a real scenario with Neon/PostgreSQL, we'd use Alembic
    # For now, we ensure tables are created
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
