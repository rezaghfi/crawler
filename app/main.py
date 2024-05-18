from fastapi import FastAPI
from database.db import *

app = FastAPI()

@app.get('/')
def root():
  return {f'hello this crawler and scraper of website snn.ir'}

# create api for counter of table counter
@app.get('/count')
def count_rows_of_database():
  rows = 3
  return {f'count of pages table: {rows}'}

# create api for csv
@app.get('/get_csv_data')
def get_csv_data():
  # read csv
  
  

