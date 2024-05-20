from fastapi import FastAPI
from sqlalchemy import Date
from app import WebsiteScraper
import datetime
from pydantic import BaseModel
import threading
import uvicorn


app = FastAPI()

@app.get('/')
def root():
  return {f' /count show data in table - /csv send filtered information to kafka'}


# create api for counter of table counter
@app.get('/count')
def count_rows_of_database():
  rows = WebsiteScraper.WebsiteScraper.extract_count_from_database()
  return {f'{"pagecount":"{rows}"}'}

class Item(BaseModel):
  date: datetime.date

# create api for csv
@app.post('/csv/')
async def csv_output_of_database(item: Item):
  #show data
  data = WebsiteScraper.WebsiteScraper.extract_data_from_database(item.date)
  return {f'This API sends information that save before {item.date} day to kafka'}

def run_fastapi():
  uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
  
# if __name__ == "__main__":
#   # uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
#   t1 = threading.Thread(target=run_fastapi, name='t1', daemon=True)
#   t2 = threading.Thread(target=WebsiteScraper.WebsiteScraper.extract_data, name='t2')
#   t1.start()
#   t2.start()

#   t1.join()
#   t2.join()

#   print("Done!")