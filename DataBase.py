from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import USER,PORT,HOST,PASSWORD, DATABASE
# print(USER,PORT,HOST,PASSWORD,DATABASE)


# # Creer la base
# DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/test"
# engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")

# with engine.connect() as conn:
#     conn.execute(text(f"CREATE DATABASE {DATABASE}"))

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL, isolation_level='AUTOCOMMIT')

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
Session = SessionLocal()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()