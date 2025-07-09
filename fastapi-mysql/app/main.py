from fastapi import FastAPI
import os
import mysql.connector

app = FastAPI()

@app.get("/")
def root():
    db = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
    cursor = db.cursor()
    cursor.execute("SELECT 1;")
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return {"db_value": result[0]}
