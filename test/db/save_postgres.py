import requests
from bs4 import BeautifulSoup
import psycopg2

# Function to fetch HTML content of a URL
def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

# Function to save HTML content into PostgreSQL
def save_html_content(url, content):
    conn = psycopg2.connect("dbname=website_content user=postgres password=1 host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO html_pages (url, content) VALUES (%s, %s)", (url, content))
    conn.commit()
    conn.close()

# Function to crawl all pages of a website
def crawl_website(base_url):
    html_content = fetch_html_content(base_url)
    if html_content:
        save_html_content(base_url, html_content)
        soup = BeautifulSoup(html_content, 'html.parser')
        for link in soup.find_all('a'):
            next_url = link.get('href')
            print(next_url)
            if next_url and next_url.startswith(base_url):
                next_url = main_url + next_url
                print("-------------"+next_url)
                crawl_website(next_url)

# Start crawling from the main page of the website
main_url = 'http://snn.ir/'
crawl_website(main_url)