from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Welcome to stock return analysis tool! Please start by choosing a stock ticker below lol"
    }


@app.get("/{ticker_name}")
async def query(ticker_name):
    """Execute a SQL query from the Stocks database to find out the growth of the stock price of a company over a 5-year period."""

    result = querydb(ticker_name)
    return {
        "The growth of the stock price of the {} over a 5-year period: {}".format(
            ticker_name, result
        )
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
