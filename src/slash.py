"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

import argparse
# import scraper
import formatter
from tabulate import tabulate
from scraper import scrape


def main():
    parser = argparse.ArgumentParser(description="Slash")
    parser.add_argument('--search', type=str, help='Product search query')
    parser.add_argument('--num', type=int, help="Maximum number of records", default=3)
    parser.add_argument('--sort', type=str, nargs='+', help="Sort according to re (relevance: default), pr (price) or ra (rating)", default="re")
    parser.add_argument('--link', action='store_true', help="Show links in the table")
    parser.add_argument('--des', action='store_true', help="Sort in descending (non-increasing) order")
    args = parser.parse_args()

    products = scrape(args, ['walmart', 'amazon'])


    print()
    print()
    print(tabulate(products, headers="keys", tablefmt="github"))
    print()
    print()

if __name__ == '__main__':
    main()