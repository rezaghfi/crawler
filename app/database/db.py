from sqlalchemy import create_engine
from sqlalchemy import insert
from models import page_table


class DB():

  # insert data to pages table
  @staticmethod
  def insert_db(url, path, html, text):
      engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
      stmt = insert(page_table).values(url=url, path=path, html=html, text=text)
      with engine.connect() as conn:
          result = conn.execute(stmt)
          conn.commit()

  # read data with filter in time
  @staticmethod
  def select_csv_db():
      engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
      stmt = page_table.select()
      with engine.connect() as conn:
          result = conn.execute(stmt)
          conn.commit()
      for row in result:
          print(row)
