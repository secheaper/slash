import json
import os
import pandas as pd
import scraper

class full_version:
	def __init__(self):
		self.data={}
		self.name=""
		self.email=""
		self.user_data = os.path.join(
			os.path.dirname(
				os.path.dirname(
					os.path.abspath(__file__))),
			"json", 
			"user_data.json"
			)
		self.df=pd.DataFrame()
		pd.set_option('display.max_rows', None)
		pd.set_option('display.max_columns', None)
		pd.set_option('display.width', None)
		pd.set_option('display.max_colwidth', 40)


	def login(self):
		if not os.path.exists(self.user_data):
			print("Welcome to Slash!")
			print("Please enter the following information: ")
			name=input("Name: ")
			email=input("Email: ")
			self.data['name']=name
			self.data['email']=email
			with open(self.user_data, 'w') as outfile:
				json.dump(self.data, outfile)
			self.name=name
			self.email=email
		else:
			with open(self.user_data) as json_file:
				data = json.load(json_file)
				self.name=data['name']
				self.email=data['email']
		return self.name, self.email

	def search_fn(self):
		prod=input("Enter name of product to Search: ")
		self.scrape(prod)
		pass

	def extract_list(self):
		pass

	def scrape(self,prod):
		products_1 = scraper.searchAmazon(prod,1)
		products_2 = scraper.searchWalmart(prod,1)
		products_3 = scraper.searchEtsy(prod,1)
		results=products_1+products_2+products_3
		#esults = formatter.sortList(results, "ra" , True)
		self.df=pd.DataFrame.from_dict(results, orient='columns')
		print(self.df)



	def driver(self):
		self.login()
		flag_loop=1
		print("Welcome ",self.name)
		while flag_loop==1:
			print("Select from following:")
			print("1. Search new product\n2. See exiting list\n3. Exit")
			choice=int(input())
			if choice==1:
				self.search_fn()
			elif choice==2:
				self.extract_list()
			elif choice==3:
				print("Thank You for Using Slash")
				flag_loop = 0
			else:
				rint("Incorrect Option")