## :money_with_wings: Slash

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Run Python Tests](https://github.com/secheaper/cheaper/blob/main/.github/workflows/python-app.yml/badge.svg?branch=Moksh-17-Sept-Adding_Test_Cases)](https://github.com/secheaper/cheaper/blob/main/.github/workflows/python-app.yml) [![DOI](https://zenodo.org/badge/407550383.svg)](https://zenodo.org/badge/latestdoi/407550383)


Stop wasting time and money — Slash helps you find the best deals online.
Slash is an upcoming chrome extension and API that scrapes the most popular e-commerce websites to get the best deals on the searched items across these websites.

![Alt Text](https://media.giphy.com/media/3ohze3cqkv058SUy2s/giphy.gif?cid=ecf05e471lrcuf3ucso5i3yrucua074n5wqx1m12t41a4h92&rid=giphy.gif&ct=g)

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

