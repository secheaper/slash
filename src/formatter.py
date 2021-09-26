from datetime import datetime
import math

def formatResult(website, titles, prices, links):
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
    if sortBy == "pr":
        return sorted(arr, key=lambda x: getNumbers(x["price"]), reverse=reverse)
    elif sortBy == "ra":
        # return sorted(arr, key=lambda x: getNumbers(x.price), reverse=reverse)
        pass
    return arr

def formatSearchQuery(query):
    return query.replace(" ", "+")

def formatTitle(title):
    if(len(title) > 40):
        return title[:40] + "..."
    return title

def getNumbers(st):
    ans = ''
    for ch in st:
        if (ch >= '0' and ch <= '9') or ch == '.':
            ans += ch
    try:
        ans = float(ans)
    except:
        ans = math.inf
    return ans