from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_CONFIG

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(
    DATABASE_CONFIG["dialect"],
    DATABASE_CONFIG["connector"],
    DATABASE_CONFIG["user"],
    DATABASE_CONFIG["password"],
    DATABASE_CONFIG["host"],
    DATABASE_CONFIG["port"],
    DATABASE_CONFIG["database"],
)
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)
