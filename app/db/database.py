from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

DATABASE_URL = "postgresql+psycopg2://rhuan_dev:AxR256396dd@localhost/workout_db"


engine = create_engine(DATABASE_URL, pool_recycle=3600, echo=False)


SessionLocal = sessionmaker(
    autoflush= False , bind= engine
)

def get_database():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()