import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.database.db import *

# all parameter use for plain database



class WebsiteScraper():
  

  # extract data is function for extract url of web page , path of page in website , html code of page , text of content page
  # function return plain_datas it is array of dictionary of four param it declared,
  def extract_data():
    base_url = "https://www.snn.ir"    
    urls = []
    urls.append(base_url)
    response = requests.get(base_url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, "html.parser")
      DB.insert_db(base_url, "/", response.text, soup.get_text())
      
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
            DB.insert_db(url, path, html, text)