from fastapi import FastAPI
from app.website_scraping_crawling import WebsiteScraper
import datetime
import uvicorn


app = FastAPI()

@app.get('/')
def root():
  return {f' /count show data in table - /output send filtered information to kafka'}


# create api for counter of table counter
@app.get('/count')
def count_rows_of_database():
  rows = WebsiteScraper.extract_count_from_database()
  return {"pagecount":f'{rows}'}


# create api for csv
@app.get('/output/{fromdate}/{todate}')
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