from sqlalchemy import func, create_engine, insert, select
from sqlalchemy.sql import func
from Model import page_table
import csv


class Database:



  #use count function to counter rows
  @staticmethod
  def count_of_table():
    engine = create_engine("postgresql://postgres:1@db:5432/website_content")
    # Create a connection
    conn = engine.connect()

    # Perform a select query
    query = select(func.count()).select_from(page_table)
    result = conn.execute(query).fetchall()
    result = result[0][0]
    return result
  
  # read data with filter in time
  @staticmethod
  def extract_excel_from_database(fromdate, todate):
    engine = create_engine("postgresql://postgres:1@db:5432/website_content")
    # Create a connection
    conn = engine.connect()

    # Perform a select query
    query = select(Model.page_table).where((page_table.c.created_at <= fromdate) & (page_table.c.created_at >= todate))
    result = conn.execute(query)

    # Specify the file path to save the data
    file_path = "./output.csv"

    # Write the result to a CSV file
    with open(file_path, "w", newline="", encoding="utf-8") as file:
      csv_writer = csv.writer(file)
      csv_writer.writerow(result.keys())  # Write the column headers
      csv_writer.writerows(result)

    print(f"Data saved to {file_path}")


