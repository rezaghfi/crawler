from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import insert





metadata = MetaData()

page_table = Table(
    'pages',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('url', String),
    Column('path', String),
    Column('html', String),
    Column('text', String)
)

def insert_db(url, path, html, text):
    engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
    stmt = insert(page_table).values(url= url, path=path, html=html, text=text)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

insert_db('/',"dfdf",'df','dfdf')