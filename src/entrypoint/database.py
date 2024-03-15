import os
from dotenv import load_dotenv

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()


DB_DRIVER = os.getenv('DB_DRIVER')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


# SQLALCHEMY_URL = "mysql+pymysql://username:password@host/schema_name"
SQLALCHEMY_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = sa.create_engine(SQLALCHEMY_URL)
Base = declarative_base()
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionFactory()

    try:
        return db
    except:
        db.rollback()

    finally:
        db.close()
        
        
        
        
        
def check_db_connection():
    try:
        db = SessionFactory()
        result = db.execute(sa.text("SELECT 1"))
        print(result.scalar())
        db.close()
        print("Connection to DataBase successfull")
    except Exception as e:
        print("DB Connection failed:", e)
        
