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
        titles, prices, links = res.select("h2 a span"), res.select("span.a-price span"), res.select("h2 a.a-link-normal")
        product = formatResult("amazon",  titles, prices, links)
        products.append(product)
    return buildResult(products)

def searchWalmart(query):
    # query = formatSearchQuery(query)
    URL = f'https://www.walmart.com/search?q={query}'
    page = httpsGet(URL)
    results = page.findAll("div", {"data-item-id":True})
    products = []
    for res in results:
        titles, prices, links = res.select("span.lh-title"), res.select("div.lh-copy"), res.select("a")
        product = formatResult("walmart", titles, prices, links)
        products.append(product)
    return buildResult(products)

def buildResult(arr):
    # first index has the most relevant search result.
    # this can be made better
    return arr[:2]

def formatResult(website, titles, prices, links):
    title, price, link = '', '', ''
    if titles: title = titles[0].get_text().strip()
    if prices: price = prices[0].get_text().strip()
    if links: link = links[0]['href']
    product = {"title": title, "price": price, "link":f'www.{website}.com{link}', "website": website}
    print(product)
    return product

def formatSearchQuery(query):
    # this could be removed
    return query.replace(" ", "+")