import requests
from bs4 import BeautifulSoup

def httpsGet(URL):
    print(URL)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    return BeautifulSoup(soup1.prettify(), "html.parser") 

def searchAmazon(query):
    # query = formatSearchQuery(query)
    URL = f'https://www.amazon.com/s?k={query}'
    page = httpsGet(URL)
    results = page.findAll("div", {"data-component-type":"s-search-result"})
    products = []
    for res in results:
        title = res.select("h2 a span")[0].get_text().strip()
        price = res.select("span.a-price span")[0].get_text().strip()
        products.append({"title": title, "price": price, "link":"www.amazon.com", "website":"amazon"})
    return buildResult(products)

def searchWalmart(query):
    # query = formatSearchQuery(query)
    URL = f'https://www.walmart.com/search?q={query}'
    page = httpsGet(URL)
    results = page.findAll("div", {"data-item-id":True})
    products = []
    for res in results:
        title = res.select("span.lh-title")[0].get_text().strip()
        price = res.select("div.lh-copy")[0].get_text().strip()
        products.append({"title": title, "price": price, "link":"www.walmart.com", "website":"walmart"})
    return buildResult(products)

def buildResult(arr):
    # first index has the most relevant search result.
    # this can be made better
    return arr[0] 

def formatSearchQuery(query):
    # this could be removed
    return query.replace(" ", "+")