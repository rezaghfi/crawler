from sqlalchemy.orm import sessionmaker
from models import Page

# Create the engine and session
engine = create_engine('postgresql://postgres:1@localhost:5432/website_content')
Session = sessionmaker(bind=engine)
session = Session()

# Insert a new user with auto-generated timestamp
new_page = Page(url = "www.snn.ir", path="/", html="hdfdf", text="dfdfdf")
session.add(new_page)
session.commit()

