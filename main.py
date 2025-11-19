from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()

#define request body schema
class Course(BaseModel):
    name: str
    instractior: str
    duration: float
    website: HttpUrl

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database='aiquest', user='aonkonmallick',password='1234', 
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('succesfully conected database')
        break
    except Exception as error:
        print('database connect failed')
        print("error: ",error)
        time.sleep(2)

@app.post("/post")
def create_post(post:Course):
    return{"data" : post}

@app.get("/")
def aiquest():
    cursor.execute(""" SELECT * FROM course """)
    data = cursor.fetchall()
    return{"Data": data }

@app.get("/text/1")
def aiquest1():
    return{"text" : "welcome to FastAPI"}