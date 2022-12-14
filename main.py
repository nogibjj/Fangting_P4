from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello visitor! \nYou can query: \n1. /query_year/{year}\n2. /query_covid/{date}"}
    
@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    """Add two numbers together"""
    total = num1 + num2
    return {"total": total}
    
@app.get("/query_year/{year}")
async def query_year(year: str):
    """query interesting facts happened in a given year"""

    url = "https://numbersapi.p.rapidapi.com/" + year + "/year"

    querystring = {'fragment': 'true', 'json': 'true'}

    headers = {
        "X-RapidAPI-Key": "155edcf844msh7d2f8265bf24668p17f256jsn999e77a74d46",
        "X-RapidAPI-Host": "numbersapi.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=10)

    return {"result": response.text}

@app.get("/query_covid/{date}")
async def query(date: str):
    """Query covid-19 statistics by date (yyyy-mm-dd)"""

    url = "https://rapidapi.com/axisbits-axisbits-default/api/covid-19-statistics/"

    querystring = {"query": date}

    headers = {
        "X-RapidAPI-Key": "155edcf844msh7d2f8265bf24668p17f256jsn999e77a74d46",
        "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=10)

    return {"result": response.text}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
