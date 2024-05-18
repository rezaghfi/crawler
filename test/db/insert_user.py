from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import insert

engine = create_engine("postgresql://postgres:1@localhost/website_content")
metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("fullname", String),
)


stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
