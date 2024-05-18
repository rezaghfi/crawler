from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy import insert, select
from . import Model


class Database:

  # insert data to pages table
  @staticmethod
  def insert_db(url, path, html, text):
    engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
    stmt = insert(Model.page_table).values(url=url, path=path, html=html, text=text)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


  # read data with filter in time
  @staticmethod
  def select_csv_db(date):
    engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
    stmt = Model.page_table.select()
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
    print(type(result))
    return result

  @staticmethod
  def count_of_table():
    engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
    stmt = select(func.count(Model.page_table.c.id))
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
    return result