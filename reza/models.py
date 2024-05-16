from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Page(Base):
    __tablename__ = 'html_pages'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    url = Column(String)
    html = Column(String)
    text = Column(String)
    created_time = Column(DateTime, default=func.now())
