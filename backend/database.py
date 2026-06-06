from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Use /tmp on Render (always writable), fallback to local db/ for dev
DB_PATH = "/tmp/url_shortener.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to get DB session in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def run_migrations():
    """Safely add new columns to existing database without losing data."""
    with engine.connect() as conn:
        # Add 'summary' column if it doesn't exist
        try:
            conn.execute(text("ALTER TABLE urls ADD COLUMN summary VARCHAR(500)"))
            conn.commit()
            logger.info("Migration: added 'summary' column to urls table.")
        except Exception:
            pass  # Column already exists — safe to ignore
