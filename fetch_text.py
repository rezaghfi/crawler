import requests
from bs4 import BeautifulSoup

def fetch_text_content(url):
  response = requests.get(url)
  if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the text content of the page
    text_content = soup.get_text()
    return text_content
  
  return None
  
url = "https://snn.ir"
output = fetch_text_content(url)
print(output)