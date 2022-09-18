from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to ETH land! Please start search the latest ETH transactions!"}

@app.get("/query")
async def query():
    """Execute a SQL query from Walmart database to search the latest ETH transactions that includes holidays and non-hoildays"""

    result = querydb()
    return {"Latest ETH transactions information": result}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')