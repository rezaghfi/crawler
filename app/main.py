from fastapi import FastAPI
from sqlalchemy import Date
from . import WebsiteScraper
import datetime
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def root():
  WebsiteScraper.WebsiteScraper.extract_data()  
  return {f'hello this crawler and scraper of website snn.ir'}

# create api for counter of table counter
@app.get('/count')
async def count_rows_of_database():
  rows = WebsiteScraper.WebsiteScraper.extract_count_from_database()
  return {f'count of pages table: {rows}'}

class Item(BaseModel):
  date: datetime.date

# create api for csv
@app.post('/csv/')
async def csv_output_of_database(item: Item):
  #show data
  return {f'This API sends information that save before {item.date} day to kafka'}