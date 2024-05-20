import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlalchemy import func, create_engine, insert, select
from sqlalchemy.sql import func
import Model

def extract_data():
    base_url = "https://www.snn.ir"    
    urls = []
    urls.append(base_url)
    response = requests.get(base_url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, "html.parser")
      insert_db(base_url, "/", response.text, soup.get_text())
      
      for link in soup.find_all("a", href=True):
        next_url = urljoin(base_url, link["href"])
        if next_url.startswith(base_url) and next_url not in urls:
          urls.append(next_url)
          res = requests.get(next_url)
          if res.status_code == 200:

            url = next_url

            path = link["href"]

            html = res.text
            
            # Parse the HTML content of the page
            soup = BeautifulSoup(html, 'html.parser')
            # Find and extract the text content of the page
            text = soup.get_text()

            #save in db 
            insert_db(url, path, html, text)
            #---------------send to kafka------------------ 
            ##############################################

def insert_db(url, path, html, text):
  engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
  stmt = insert(Model.page_table).values(url=url, path=path, html=html, text=text)
  with engine.connect() as conn:
      conn.execute(stmt)
      conn.commit()

extract_data()