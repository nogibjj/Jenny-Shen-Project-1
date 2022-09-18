from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to stock return analysis tool! Please start by choosing a stock ticker lol"}

@app.get("/query")
async def query():
    """Execute a SQL query from the Stocks database to find out the average daily return of a specific stock"""

    result = querydb()
    return {"Average daily return of the ": result}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')