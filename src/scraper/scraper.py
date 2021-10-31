# package imports
from bs4 import BeautifulSoup
import requests

# local imports
import src.formatter as formatter
from src.scraper.configs import AMAZON, WALMART


def httpsGet(URL):
    """makes HTTP called to the requested URL with custom headers

    Parameters
    ----------
    URL: str
        URL we are sending request to

    Returns
    ----------
    soup: str
        HTML of page we requested
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',  # noqa: E501
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'DNT': '1',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }
    page = requests.get(URL, headers=headers)
    # TODO check for page status
    soup1 = BeautifulSoup(page.content, 'html.parser')
    return BeautifulSoup(soup1.prettify(), 'html.parser')


def search(query, config):
    """Scrape the given config for a specific item

    Parameters
    ----------
    query: str
        Query of item we are looking for
    config: dict
        Configuration for site we are scraping

    Returns
    ----------
    products: list
        List of items returned from website
    """

    query = formatter.formatSearchQuery(query)
    URL = config['url'] + query
    page = httpsGet(URL)
    results = page.find_all(config['item_component'], config['item_indicator'])
    products = []
    for res in results:
        title = res.select(config['title_indicator'])
        price = res.select(config['price_indicator'])
        link = res.select(config['link_indicator'])
        product = formatter.formatResult(config['site'], title, price, link)
        products.append(product)
    return products


def scrape(args, scrapers):
    """Conduct scraping of sites based on scrapers

    Parameters
    ----------
    args: dict
        Dictionary of arguments used for scraping
    scrapers: list
        List of scrapers to use

    Returns
    ----------
    overall: list
        List of items returned from scrapers
    """

    query = args.search

    overall = []
    for scraper in scrapers:
        if scraper == 'walmart':
            local = search(query, WALMART)
        elif scraper == 'amazon':
            local = search(query, AMAZON)
        elif scraper == 'target':
            # TODO finish target scraper
            local = []
        else:
            continue

        for sort_by in args.sort:
            local = formatter.sortList(local, sort_by, args.des)[:args.num]
        overall.extend(local)

    for sort_by in args.sort:
        overall = formatter.sortList(overall, sort_by, args.des)

    return overall
