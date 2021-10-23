from typing import Optional
import scraper
from fastapi import FastAPI
import json 
import logging
# Open function to open the file "MyFile1.txt"  
# (same directory) in read mode and 



app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/az/{item_name}")
async def searchAmazonAPI(item_name: str, q: Optional[str] = None):
    file1 = open("logger.txt", "a")
    file1.write('amazon query:' + str(item_name)+'\n')
    itemList = scraper.searchAmazon(item_name)
    itemListJson = json.dumps(itemList) 
    file1.close()
    return itemListJson





