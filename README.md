<p align="center"><img width="500" src="./assets/slash.png"></p>

![GitHub](https://img.shields.io/github/license/secheaper/slash)
![github workflow](https://github.com/secheaper/cheaper/actions/workflows/python-app.yml/badge.svg) 
[![DOI](https://zenodo.org/badge/407550383.svg)](https://zenodo.org/badge/latestdoi/407550383)
![Github](https://img.shields.io/badge/language-python-red.svg)
![GitHub issues](https://img.shields.io/github/issues-raw/secheaper/slash)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/secheaper/slash)
![Github pull requests](https://img.shields.io/github/issues-pr/secheaper/slash)
![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/secheaper/slash)
[![codecov](https://codecov.io/gh/secheaper/slash/branch/main/graph/badge.svg?token=I2J7ICDDI9)](https://codecov.io/gh/secheaper/slash)

Slash is a command line tool that scrapes the most popular e-commerce websites to get the best deals on the searched items across these websites. 
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash uses very easy commands to filter, sort and search your items
- **Powerful**: Quickly alter the commands to get desired results

<p align="center">
  <a href="#rocket-installation">Installation</a>
  ::
  <a href="#golf-flags-and-command-line-arguments">Flags & Args</a>
  ::
  <a href="#card_index_dividers-some-examples">Examples</a>
  ::
  <a href="#thought_balloon-use-case">Use Case</a>
  ::
  <a href="#page_facing_up-why">Why</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
    ::
  <a href="#email-support">Support</a>
  
</p>

---

<p align="center"><img width="700" src="./assets/demo.gif"></p>

---

:rocket: Installation
---
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/secheaper/slash.git
cd slash
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip3 install -r requirements.txt
```
4. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the python command to run the ```slash.py``` file.
```
cd src

For Mac
python3 slash.py --search socks

For Windows
python slash.py --search socks
```
:golf: Flags and Command Line Arguments
---
Currently the tool supports the following flags and command line arguments. These flags and arguments can be used to quickly filter and guide the search to get you the best results very quickly.

| Arguments | Type | Default | Description                                                          |
|-----------|------|---------|----------------------------------------------------------------------|
| --search  | str  | None    | The product name to be used as the search query                      |
| --num     | int  | 3       | Maximum number of products to search                                 |
| --sort    | str  | re      | Sort results by relevance (re) or by price (pr)                      |
| --des     | bool | -       | Set boolean flag if results should be sorted in non-increasing order |

:card_index_dividers: Some Examples
---

#### 1. Searching
```--search```  accepts one argument string which it uses to search and scrape the requested products on 
the e-commerce websites. So, to use this, run the python script followed by the --search argument and the 
search string. The search string should be in double quotes if it have two or more words. Example:
```
For Mac
python3 slash.py --search "philips hue"

For Windows
python slash.py --search "philips hue"
```
```
| timestamp           | title                                       | price   | website   |
|---------------------|---------------------------------------------|---------|-----------|
| 30/09/2021 12:00:58 | Philips Hue White and Color Ambiance A19... | $134.99 | amazon    |
| 30/09/2021 12:00:58 | PARMIDA LED 5/6 inch Smart Recessed Ligh... | $20.99  | amazon    |
| 30/09/2021 12:00:58 | Philips Hue 548610 CFH Smart Light A19, ... | $79.99  | amazon    |
| 30/09/2021 12:01:00 | Philips Hue 3-Pack 60W White Bluetooth S... | $37.88  | walmart   |
| 30/09/2021 12:01:00 | Philips Hue Smart Stand Alone Bridge, Hu... | $57.92  | walmart   |
| 30/09/2021 12:01:00 | Philips Hue White and Color Ambiance Sma... | $89.99  | walmart   |
```
#### 2. Sorting
```--sort``` accepts one or more arguments that determine how the tool sorts and filters the requested products
after scraping. The first value is used to initially sort and filter the results of the scraping. The arguments
following the first one are not required but will be used to further sort the filtered results. Example:
```
For Mac
python3 slash.py --search "philips hue" --sort pr

For Windows
python slash.py --search "philips hue" --sort pr
```
```
| timestamp           | title                                       | price   | website   |
|---------------------|---------------------------------------------|---------|-----------|
| 30/09/2021 12:02:34 | Philips Hue White A19 60W Smart Dimmable... | $14.88  | walmart   |
| 30/09/2021 12:02:33 | T POWER 24V Ac Dc Adapter Charger Compat... | $16.99  | amazon    |
| 30/09/2021 12:02:33 | Philips Hue 1748930VN 8ft Cable Connecto... | $19.99  | amazon    |
| 30/09/2021 12:02:32 | PARMIDA LED 5/6 inch Smart Recessed Ligh... | $20.99  | amazon    |
| 30/09/2021 12:02:34 | Philips Hue White Ambiance A19 Smart Lig... | $24.99  | walmart   |
| 30/09/2021 12:02:34 | Philips Hue White and Color Ambiance Sma... | $29.99  | walmart   |
```
#### 3. Sort Order
The ```--des``` flag can be set to sort the requested products in a non-increasing order. This flag will be 
actually used when coupled with ```--sort```. Example:
```
For Mac
python3 slash.py --search "philips hue" --sort pr --des

For Windows
python slash.py --search "philips hue" --sort pr --des
```
```
| timestamp           | title                                       | price   | website   |
|---------------------|---------------------------------------------|---------|-----------|
| 30/09/2021 12:03:42 | Philips Hue Bluetooth Smart Lightstrip P... |         | amazon    |
| 30/09/2021 12:03:42 | Philips - Hue Play HDMI Sync Box - Black... |         | amazon    |
| 30/09/2021 12:03:42 | Lutron Aurora Smart Bulb Dimmer Switch |... |         | amazon    |
| 30/09/2021 12:03:44 | Philips Hue White and Color Ambiance A19... | $199.99 | walmart   |
| 30/09/2021 12:03:44 | Philips Hue White and Color Ambiance 2-P... | $105.87 | walmart   |
| 30/09/2021 12:03:44 | Philips Hue White and Color Ambiance Sma... | $89.99  | walmart   |
```

#### 4. Result length
The maximum number of results that are scraped from each website can be set using the ```--num``` argument. It accepts
an integer value ```n``` and then returns ```n``` results from each website. Note that tool returns a maximum of 
the value of ```n``` and the number of results on the webiste. By default this value is set to 3. Example:
```
For Mac
python3 slash.py --search "philips hue" --num 5

For Windows
python slash.py --search "philips hue" --num 5
```
```
| timestamp           | title                                       | price   | website   |
|---------------------|---------------------------------------------|---------|-----------|
| 30/09/2021 12:07:41 | Govee Immersion TV LED Backlights with C... | $82.99  | amazon    |
| 30/09/2021 12:07:41 | Philips Hue 548610 CFH Smart Light A19, ... | $79.99  | amazon    |
| 30/09/2021 12:07:41 | Philips Hue Play White & Color Smart Lig... | $149.99 | amazon    |
| 30/09/2021 12:07:41 | Philips Hue White and Color Iris Corded ... | $99.99  | amazon    |
| 30/09/2021 12:07:41 | Philips Hue White & Color E12 LED Candle... | $49.97  | amazon    |
| 30/09/2021 12:07:42 | Philips Hue 3-Pack 60W White Bluetooth S... | $37.88  | walmart   |
| 30/09/2021 12:07:42 | Philips Hue Smart Stand Alone Bridge, Hu... | $57.92  | walmart   |
| 30/09/2021 12:07:42 | Philips Hue White and Color Ambiance Sma... | $89.99  | walmart   |
| 30/09/2021 12:07:42 | Philips Hue White and Color Ambiance Sma... | $29.99  | walmart   |
| 30/09/2021 12:07:42 | Philips Hue White and Color Ambiance A19... | $199.99 | walmart   |
```

:thought_balloon: Use Case
---
* ***Students***: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
* ***Data Analysts***: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually inportant.

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!
- Slash in its current form is for people who have some understanding of python and are comfortable in using the command line interface to interact with systems.
- Future updates aim to encompass a wide variety of users irrespective of their computer knowledge and background.


:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="http://www.shubhammankar.com/"><img src="https://avatars.githubusercontent.com/u/29366125?v=4" width="75px;" alt=""/><br /><sub><b>Anant Gadodia</b></sub></a></td>
    <td align="center"><a href="https://github.com/pratikdevnani"><img src="https://avatars.githubusercontent.com/u/43350493?v=4" width="75px;" alt=""/><br /><sub><b>Anmolika Goyal</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/moksh98"><img src="https://avatars.githubusercontent.com/u/29693765?v=4" width="75px;" alt=""/><br /><sub><b>Shubhangi Jain</b></sub></a><br /></td>
    <td align="center"><a href="https://rahilsarvaiya.tech/"><img src="https://avatars0.githubusercontent.com/u/32304956?v=4" width="75px;" alt=""/><br /><sub><b>Shreya Karra</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/annie0467"><img src="https://avatars.githubusercontent.com/u/17164255?v=4" width="75px;" alt=""/><br /><sub><b>Srujana Rao</b></sub></a><br /></td>
  </tr>
</table>

:email: Support
---

For any queries and help, please reach out to us at: secheaper@gmail.com
