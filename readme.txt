1.write crawler
2.save in database
3.create fastapi
4.create two api
5.create dockerfile and docker compose
6.create kafka
7.send csv to kafka

# start 
python -m venv .venv/
source Script/activate
pip install -r requirement.txt
uvicorn app.main:app --reload