from sqlalchemy import MetaData, Table, Column, Integer, Text

metadata = MetaData()

page_table = Table(
    'pages',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('url', Text),
    Column('path', Text),
    Column('html', Text),
    Column('text', Text)
)