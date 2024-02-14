from fastapi import FastAPI
from os import getenv
from dotenv import load_dotenv


load_dotenv()
API_KEY = getenv('API_KEY')

app = FastAPI()


@app.get('/')
def hello():
    return {'hello': 'world'}
