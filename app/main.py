from fastapi import FastAPI
from sqlalchemy import Date
from . import WebsiteScraper
import datetime
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def root():
  return {f' /count show data in table - /csv send filtered information to kafka'}


# create api for counter of table counter
@app.get('/count')
def count_rows_of_database():
  rows = WebsiteScraper.WebsiteScraper.extract_count_from_database()
  return {f'count pages of website is: {rows}'}

class Item(BaseModel):
  date: datetime.date

# create api for csv
@app.post('/csv/')
async def csv_output_of_database(item: Item):
  #show data
  data = WebsiteScraper.WebsiteScraper.extract_data_from_database(item.date)
  return {f'This API sends information that save before {item.date} day to kafka'}