import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# all parameter use for plain database
base_url = 'http://www.snn.ir/'

# استخراج کد از روی آدرس
# Function to fetch HTML content of a URL
def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

# Function to get all page URLs from a website
def extract_data(base_url):
  plain_datas = []
  urls = []
  urls.append(base_url)
  response = requests.get(base_url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    plain_datas.append({"path": "/", "url": base_url, "html": response.text, "content": response.text})
    for link in soup.find_all('a', href=True):
        url = None
        path = None
        content = None
        html = None
        path = link['href']
        next_url = urljoin(base_url, link['href'])
        if next_url.startswith(base_url) and next_url not in urls:
            urls.append(next_url)
            url = next_url

  return plain_datas

datas = extract_data(base_url)
for data in datas:
  for key, value in data.items():
      print(f"{key}: {value}")

