# IDS 706 Project 1
![end-of-day-stock-prices](https://user-images.githubusercontent.com/112578566/190939521-3c378ec8-3edc-4d57-b429-952fda1f2058.png)

## Background and dataset
This project grabs a Kaggle dataset that oulines the historical stock data for all current S&P 500 companies. This dataset include data up to Feb 2018. (https://www.kaggle.com/datasets/camnugent/sandp500).

![Screen Shot 2022-09-18 at 9 55 14 PM](https://user-images.githubusercontent.com/112578566/190938739-5d262833-ba02-47ca-b60b-1d3cdf8e92ee.png)


In fiancial worlds, people are interested in finding out the return of an investment they made, and stock price growth is a great indicator for measuring this. Therefore, in project 1, I'm trying to output the growth rate of a company by inputing its specific stock ticker.

![Rate-of-Return-on-Investment](https://user-images.githubusercontent.com/112578566/190937423-71029c28-28a3-475c-a47c-aa9df92b25dc.jpeg)

## Connect Databricks cluster to Github Codespace
![Screen Shot 2022-09-18 at 10 01 32 PM](https://user-images.githubusercontent.com/112578566/190939078-4116eead-8cc2-45df-9819-bbda5089a456.png)


## Scaffolds
```
README.md
Makefile
requirements.txt
.devcontainer
helpers.py
querydb.py
query_sql_db.py
```

## Test out Cli
```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```

## Microservices via Fastapi
![Screen Shot 2022-09-18 at 10 14 47 PM](https://user-images.githubusercontent.com/112578566/190939887-ec2f11c8-0fe8-4196-8f96-de310ecb377b.png)

By typing "/" + "ticker name" after the URL, you'll get the growth of the stock price of a specific company over the past five years, which could provide us with a good indicator of whether a compnay is an ideal investment target.

![Screen Shot 2022-09-18 at 10 15 08 PM](https://user-images.githubusercontent.com/112578566/190939895-0a616876-6f64-43c6-9f08-ff2466a4ee03.png)

## More to come!
More financial analysis about this S&P 500 stock dataset including daily return of stock price return, moving average of stock price and stock price forecasting will be updated sooner...
