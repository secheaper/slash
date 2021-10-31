# package imports
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import json 
import logging

# local imports
import src.scraper.scraper as scr
from src.scraper.configs import AMAZON, WALMART

# Open function to open the file "MyFile1.txt"  
# (same directory) in read mode and 

app = FastAPI()

@app.get("/")
async def read_root():
    '''Get documentation of API

    Parameters
    ----------
    None

    Returns
    ----------
    documentation redirect
    '''
    response = RedirectResponse(url='/redoc')
    return response

@app.get("/az/{item_name}")
async def search_Amazon_API(item_name: str, q: Optional[str] = None): 
    '''Wrapper API to fetch AMAZON, WALMART and TARGET query results

    Parameters
    ----------
    item_name: string of item to be searched

    Returns
    ----------
    itemListJson: JSON List
        list of search results as JSON List
    '''
    file1 = open("logger.txt", "a")
    file1.write('amazon query:' + str(item_name)+'\n')
    itemList = scr.search(query = item_name,config= AMAZON)
    itemListJson = json.dumps(itemList) 
    file1.close()
    return itemListJson





