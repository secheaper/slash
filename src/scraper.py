"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

"""
The scraper module holds functions that actually scrape the e-commerce websites
"""

import requests
import formatter
from bs4 import BeautifulSoup
import re
import csv_writer
import csv


def httpsGet(URL):
    """
    The httpsGet function makes HTTP called to the requested URL with custom headers
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    return BeautifulSoup(soup1.prettify(), "html.parser")


def searchAmazon(query, df_flag, currency):
    """
    The searchAmazon function scrapes amazon.com
    """
    query = formatter.formatSearchQuery(query)
    URL = f'https://www.amazon.com/s?k={query}'
    page = httpsGet(URL)
    results = page.findAll("div", {"data-component-type": "s-search-result"})
    products = []
    for res in results:
        titles, prices, links = res.select("h2 a span"), res.select("span.a-price span"), res.select("h2 a.a-link-normal")
        ratings = res.select("span.a-icon-alt")
        product = formatter.formatResult("amazon",  titles, prices, links,ratings, df_flag, currency)
        products.append(product)
    return products

def searchWalmart(query, df_flag, currency):
    """
    The searchWalmart function scrapes walmart.com
    """
    query = formatter.formatSearchQuery(query)
    URL = f'https://www.walmart.com/search?q={query}'
    page = httpsGet(URL)
    results = page.findAll("div", {"data-item-id":True})
    #print(results)
    products = []
    pattern = re.compile(r'Stars')
    for res in results:
        titles, prices, links = res.select("span.lh-title"), res.select("div.lh-copy"), res.select("a")
        ratings = res.findAll("span",{"class":"w_Cj"},text=pattern)
        product = formatter.formatResult("walmart", titles, prices, links,ratings, df_flag, currency)
        products.append(product)
    return products

def searchEtsy(query, df_flag, currency):
    """
    The searchEtsy function scrapes Etsy.com
    """
    query = formatter.formatSearchQuery(query)
    url = f'https://www.etsy.com/search?q={query}'
    products = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    for item in soup.select('.wt-grid__item-xs-6'):
        titles, prices, links = (item.select("h3")), (item.select(".currency-value")), (item.select('.width-full'))
        ratings = item.select('span.screen-reader-only')
        product = formatter.formatResult("Etsy", titles, prices, links, ratings, df_flag, currency)
        products.append(product)
    return products

def driver(product, currency, num=None, df_flag=0,csv=False,cd=None):
    products_1 = searchAmazon(product,df_flag, currency)
    products_2 = searchWalmart(product,df_flag, currency)
    products_3 = searchEtsy(product,df_flag, currency)
    results=products_1+products_2+products_3
    if csv==True:

        print("CSV Saved at: ",cd)
        print("File Name:", csv_writer.write_csv(results, product, cd))
    return products_1[:num]+products_2[:num]+products_3[:num]

