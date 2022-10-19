from data_generator import data_gen_sqla
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from db import engine, Session

Base = declarative_base()


class Elasticsearch(Base):

    __tablename__ = "elasticsearch"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    age = Column(Integer, nullable=True)

    def __repr__(self) -> str:
        return super().__repr__()


Base.metadata.create_all(bind=engine)

session = Session()


data = data_gen_sqla(limit=25)
for i in data:
    elasticsearch_object = Elasticsearch(
        name=i["name"], address=i["address"], age=i["age"]
    )
    session.add_all([elasticsearch_object])
    session.commit()
