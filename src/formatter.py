import time

def formatResult(website, titles, prices, links):
    title, price, link = '', '', ''
    if titles: title = titles[0].get_text().strip()
    if prices: price = prices[0].get_text().strip()
    if links: link = links[0]['href']
    product = {
        'timestamp': round(time.time()*1000),
        "title": formatTitle(title),
        "price": price, 
        # "link":f'www.{website}.com{link}', 
        "website": website,
    }
    return product

def formatSearchQuery(query):
    return query.replace(" ", "+")

def formatTitle(title):
    if(len(title) > 40):
        return title[:40] + "..."
    return title