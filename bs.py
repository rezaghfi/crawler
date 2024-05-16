import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# all parameter use for plain database
base_url = "http://www.snn.ir/"


# extract data is function for extract url of web page , path of page in website , html code of page , text of content page
# function return plain_datas it is array of dictionary of four param it declared,
def extract_data(base_url):
  plain_datas = []
  urls = []
  urls.append(base_url)
  response = requests.get(base_url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    plain_datas.append(
      {
        "path": "/",
        "url": base_url,
        "html": response.text,
        "text_content": response.text,
      }
    )
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
          text_content = soup.get_text()

          plain_datas.append(
              {
                "path": path,
                "url": url,
                "html": html,
                "text_content": text_content,
              }
          )

    return plain_datas


datas = extract_data(base_url)
with open('crawler_output.txt', 'w') as f:
    for item in datas:
        f.write("%s\n" % item)
