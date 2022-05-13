import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username= 'root'
password='123456'
db_name='my_db'

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"


SQLALCHEMY_TRACK_MODIFICATIONS=True


SQLALCHEMY_DATABASE_URL =  f"mysql+pymysql://{username}:{password}@localhost:3306/{db_name}"


#Docker

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://fastApiUser:fastApi37Pass@0.0.0.0:3306/hzdb"

print("SQLALCHEMY_DATABASE_URL :: ", SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL#, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()
