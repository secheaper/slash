import sys
import scraper
from tabulate import tabulate


def main():
    query = sys.argv[1]
    amazonProd = scraper.searchAmazon(query)
    walmartProd = scraper.searchWalmart(query)
    results = {
        'searchedString': query.replace("+"," "),
        'results': amazonProd + walmartProd,
    }
    print()
    print()
    print(tabulate(results["results"], headers="keys"))
    print()
    print()

if __name__ == '__main__':
    main()