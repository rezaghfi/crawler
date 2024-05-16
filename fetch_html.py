import requests

def fetch_html_content(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.text
  return None

url = "https://snn.ir"
output = fetch_html_content(url)
print(output)