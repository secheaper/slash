## :money_with_wings: Slash

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Run Python Tests](https://github.com/secheaper/cheaper/blob/main/.github/workflows/python-app.yml/badge.svg?branch=Moksh-17-Sept-Adding_Test_Cases)](https://github.com/secheaper/cheaper/blob/main/.github/workflows/python-app.yml) [![DOI](https://zenodo.org/badge/407550383.svg)](https://zenodo.org/badge/latestdoi/407550383)


Stop wasting time and money — Slash helps you find the best deals online.
- Slash is an upcoming chrome extension and API that scrapes the most popular e-commerce websites to get the best deals on the searched items across these websites. 
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- The growth of e-commerce has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slashed aims to reduce by giving you a easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!


<p float="left">
<img src="https://media.giphy.com/media/3ohze3cqkv058SUy2s/giphy.gif?cid=ecf05e471lrcuf3ucso5i3yrucua074n5wqx1m12t41a4h92&rid=giphy.gif&ct=g" width= "50%" height="50%"/>
<img src="https://media.giphy.com/media/J2szWbDQaXQ6Q/giphy.gif?cid=ecf05e47sbd284u1sodsywwh4l2v5v64rfadf4kg5t0vhw3l&rid=giphy.gif&ct=g" width= "50%" height="50%"/>  
</p>

<!-- ![Alt Text](https://media.giphy.com/media/3ohze3cqkv058SUy2s/giphy.gif?cid=ecf05e471lrcuf3ucso5i3yrucua074n5wqx1m12t41a4h92&rid=giphy.gif&ct=g) ![Alt Text](https://media.giphy.com/media/J2szWbDQaXQ6Q/giphy.gif?cid=ecf05e47sbd284u1sodsywwh4l2v5v64rfadf4kg5t0vhw3l&rid=giphy.gif&ct=g) -->

### What does Slash do?
Pass any search string to the Slash API. It can be called by the following command
<pre><code>slash 'Philips Hue Bulb'</code></pre>

The API returns the prices for the searched items from e-commerce websites in JSON format

```
    {
        ts: 1630436269,
        website: 'amazon',
        searchedString: 'Philips Hue Bulb',
        results: [
            {
                title: 'Philips Hue White A21 High Lumen Smart Bulb, 1600 Lumens, Bluetooth & Zigbee compatible (Hue Hub Optional), Works with Alexa & Google Assistant',
                price: 19.99,
                currency: 'USD',
                ...
            }
        ],
        ...
    }
```

### JSON Configuration
Configuration information of the returned JSON

| Key     | Type         | Description                        |
|---------|--------------|------------------------------------|
| ts      | ```int```    | Unix timestamp in seconds          |
| website | ```string``` | Name of e-commerce website scraped |
| searchedString | ```string``` | String used to search product |
| results | ```list``` | List of results  |
| title | ```string``` | Name of the product  |
| price | ```float``` | Price of the item scraped  |
| currency | ```string``` | Currency of the returned price of item  |

