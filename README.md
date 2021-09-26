<p align="center"><img width="500" src="./assets/slash.png"></p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
![github workflow](https://github.com/secheaper/cheaper/actions/workflows/python-app.yml/badge.svg) 
[![DOI](https://zenodo.org/badge/407550383.svg)](https://zenodo.org/badge/latestdoi/407550383)
![Github](https://img.shields.io/badge/language-python-red.svg)
![GitHub issues](https://img.shields.io/github/issues-raw/secheaper/cheaper)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/secheaper/cheaper)
[![codecov](https://codecov.io/gh/secheaper/cheaper/branch/main/graph/badge.svg?token=I2J7ICDDI9)](https://codecov.io/gh/secheaper/cheaper)

Slash is a command line tool that scrapes the most popular e-commerce websites to get the best deals on the searched items across these websites. 
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash uses very easy commands to filter, sort and search your items
- **Powerful**: Quickly alter the commands to get desired results

Insert basic working .gif here

---

Installation
---
<br/> Step 1: Clone the repository and go to the directory
```
git clone https://github.com/secheaper/slash.git
cd slash
```
<br/> Step 2: Get the required packages
```
pip install -r requirements.txt
```
<br/> Step 3: Go to the source code and run
```
cd src
python3 slash.py "philips hue"
```

Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- The growth of e-commerce has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you a easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!

### What does Slash do?
Pass any search string to Slash. It can be called by the following command
<pre><code>python3 slash.py --search airpods</code></pre>

Slash returns the prices for the searched items from e-commerce websites in a tabular form

```
|     timestamp | title                                       | price   | website   |
|---------------|---------------------------------------------|---------|-----------|
| 1632601614061 | Apple AirPods with Charging Case            | $119.00 | amazon    |
| 1632601614068 | Apple AirPods Pro                           | $197.00 | amazon    |
| 1632601614073 | Apple AirPods Pro                           | $197.00 | amazon    |
| 1632601615898 | Apple AirPods Pro                           | $197.00 | walmart   |
| 1632601615899 | Apple AirPods with Charging Case (Latest... | $119.00 | walmart   |
| 1632601615899 | Apple AirPods with Wireless Charging Cas... | $159.98 | walmart   |
```
