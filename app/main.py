from fastapi import FastAPI
from sqlalchemy import Date
from app.website_scraping_crawling import WebsiteScraper
import datetime
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/')
def root():
  return {f' /count show data in table - /csv send filtered information to kafka'}

async def startup_event():
    print("Running setup tasks during startup...")
    WebsiteScraper.extract_data()

# Register the function to run during startup
@app.on_event("startup")
async def startup():
    await startup_event()

# create api for counter of table counter
@app.get('/count')
def count_rows_of_database():
  rows = WebsiteScraper.extract_count_from_database()
  return {"pagecount":f'{rows}'}


# create api for csv
@app.get('/csv/{fromdate}/{todate}')
async def csv_output_of_database(fromdate: datetime.date, todate: datetime.date):
  #show data
  data = WebsiteScraper.extract_data_from_database(fromdate, todate)
  return {f'This API save info {fromdate} day to {todate} in excel file'}

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