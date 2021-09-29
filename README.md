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
  <a href="#page_facing_up-why">Why</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
  
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
pip install -r requirements.txt
```
4. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the python command to run the ```slash.py``` file.
```
cd src
python3 slash.py --search "philips hue"
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
Pass any search string to Slash. It can be called by the following command
```
python3 slash.py --search airpods
```

Slash returns the prices for the searched items from e-commerce websites in a tabular form

```
| timestamp           | title                                       | price   | website   |
|---------------------|---------------------------------------------|---------|-----------|
| 28/09/2021 09:03:47 | Apple AirPods with Charging Case            | $119.00 | amazon    |
| 28/09/2021 09:03:47 | Apple AirPods Pro                           | $197.00 | amazon    |
| 28/09/2021 09:03:47 | Apple AirPods with Charging Case            | $119.00 | amazon    |
| 28/09/2021 09:03:49 | Apple AirPods Pro                           | $197.00 | walmart   |
| 28/09/2021 09:03:49 | Apple AirPods with Charging Case (Latest... | $119.00 | walmart   |
| 28/09/2021 09:03:49 | Apple AirPods with Wireless Charging Cas... | $159.98 | walmart   |
```

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!


:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="http://www.shubhammankar.com/"><img src="https://avatars.githubusercontent.com/u/29366125?v=4" width="75px;" alt=""/><br /><sub><b>Shubham Mankar</b></sub></a></td>
    <td align="center"><a href="https://github.com/pratikdevnani"><img src="https://avatars.githubusercontent.com/u/43350493?v=4" width="75px;" alt=""/><br /><sub><b>Pratik Devnani</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/moksh98"><img src="https://avatars.githubusercontent.com/u/29693765?v=4" width="75px;" alt=""/><br /><sub><b>Moksh Jain</b></sub></a><br /></td>
    <td align="center"><a href="https://rahilsarvaiya.tech/"><img src="https://avatars0.githubusercontent.com/u/32304956?v=4" width="75px;" alt=""/><br /><sub><b>Rahil Sarvaiya</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/annie0467"><img src="https://avatars.githubusercontent.com/u/17164255?v=4" width="75px;" alt=""/><br /><sub><b>Anushi Keswani</b></sub></a><br /></td>
  </tr>
</table>
