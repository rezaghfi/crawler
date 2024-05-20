from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, Text, Date
import csv

# Create an engine to connect to a database
engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")

# Define a metadata object
metadata = MetaData()

# Reflect the table structure from the database
pages = Table(
    "pages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("url", Text),
    Column("path", Text),
    Column("html", Text),
    Column("text", Text),
    Column("created_at", Date)
)

# Create a connection
conn = engine.connect()

# Perform a select query
query = select(pages).where(pages.c.created_at < "2005-05-05")
result = conn.execute(query)

# Specify the file path to save the data
file_path = "output.csv"

# Write the result to a CSV file
with open(file_path, "w", newline="", encoding="utf-8") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(result.keys())  # Write the column headers
    csv_writer.writerows(result)

print(f"Data saved to {file_path}")
