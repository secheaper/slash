# package imports
import uvicorn
from os import scandir
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import json 
import logging

# local imports
import scraper.scraper as scr
from scraper.configs import AMAZON, WALMART


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

@app.get("/{site}/{item_name}")
async def search_items_API(site : str,item_name: str, relevant: Optional[str] = None, order_by_col: Optional[str] = None, reverse: Optional[bool] = False, ListLengthInd: Optional[int] = 10): 
    '''Wrapper API to fetch AMAZON, WALMART and TARGET query results

    Parameters
    ----------
    item_name: string of item to be searched

    Returns
    ----------
    itemListJson: JSON List
        list of search results as JSON List
    '''
    #logging in file
    file = open("logger.txt", "a")
    file.write('amazon query:' + str(item_name)+'\n')
    
    #building argument 
    args = {
    'search': item_name,
    'sort' : 'pr' if order_by_col == 'price' else 'pr', # placeholder TDB
    'des' : reverse, # placeholder TBD
    'num' : ListLengthInd,
    'relevant' : relevant
    }

    print(args)
    scrapers = []

    if site == 'az' or site == 'all':
        scrapers.append('amazon')
    if site == 'wm' or site == 'all':
        scrapers.append('walmart')
    if site == 'tg' or site == 'all':
        scrapers.append('target')

    #calling scraper.scrape to fetch results
    itemList =  scr.scrape(args = args, scrapers= scrapers)
 
    #returning JSON list
    itemListJson = json.dumps(itemList) 
    file.close()    
    return itemListJson

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)






