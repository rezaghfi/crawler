from sqlalchemy import func, create_engine, insert, select
from sqlalchemy.sql import func
from app import Model
import csv


class Database:

  # insert data to pages table
  @staticmethod
  def insert_db(url, path, html, text):
    engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
    stmt = insert(Model.page_table).values(url=url, path=path, html=html, text=text)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

  #use count function to counter rows
  @staticmethod
  def count_of_table():
    engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
    # Create a connection
    conn = engine.connect()

    # Perform a select query
    query = select(func.count()).select_from(Model.page_table)
    result = conn.execute(query).fetchall()
    result = result[0][0]
    return result
  
  # read data with filter in time
  @staticmethod
  def extract_excel_from_database(fromdate, todate):
    engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
    # Create a connection
    conn = engine.connect()

    # Perform a select query
    query = select(Model.page_table).where((Model.page_table.c.created_at <= fromdate) & (Model.page_table.c.created_at >= todate))
    result = conn.execute(query)

    # Specify the file path to save the data
    file_path = "./output.csv"

    # Write the result to a CSV file
    with open(file_path, "w", newline="", encoding="utf-8") as file:
      csv_writer = csv.writer(file)
      csv_writer.writerow(result.keys())  # Write the column headers
      csv_writer.writerows(result)

    print(f"Data saved to {file_path}")


