"""
The formatter module focuses on processing raw text and returning it in 
the required format. 
"""

from datetime import datetime
import math

def formatResult(website, titles, prices, links):
    """
    The formatResult function takes the scraped HTML as input, and extracts the 
    necessary values from the HTML code. Ex. extracting a price '$19.99' from
    a paragraph tag.
    """
    title, price, link = '', '', ''
    if titles: title = titles[0].get_text().strip()
    if prices: price = prices[0].get_text().strip()
    if links: link = links[0]['href']
    product = {
        'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "title": formatTitle(title),
        "price": price, 
        # "link":f'www.{website}.com{link}', 
        "website": website,
    }
    return product

def sortList(arr, sortBy, reverse):
    """
    The sortList function is used to sort the products list based on the
    flags provided as args. Currently, it supports sorting by price.
    """
    if sortBy == "pr":
        return sorted(arr, key=lambda x: getNumbers(x["price"]), reverse=reverse)
    # To-do: sort by rating
    elif sortBy == "ra":
        # return sorted(arr, key=lambda x: getNumbers(x.price), reverse=reverse)
        pass
    return arr

def formatSearchQuery(query):
    """
    The formatSearchQuery function formats the search string into a string that 
    can be sent as a url paramenter.
    """
    return query.replace(" ", "+")

def formatTitle(title):
    """
    The formatTitle function formats titles extracted from the scraped HTML code.
    """
    if(len(title) > 40):
        return title[:40] + "..."
    return title

def getNumbers(st):
    """
    The getNumbers function extracts float values (price) from a string.
    Ex. it extracts 10.99 from '$10.99' or 'starting at $10.99'
    """
    ans = ''
    for ch in st:
        if (ch >= '0' and ch <= '9') or ch == '.':
            ans += ch
    try:
        ans = float(ans)
    except:
        ans = math.inf
    return ans