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
		self.user_list = os.path.join(
			os.path.dirname(
				os.path.dirname(
					os.path.abspath(__file__))),
			"csvs", 
			"user_list.csv"
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
		ch=int(input("\n\nEnter 1 to save product to list \nelse enter any other key to continue"))
		if ch==1:
			indx=int(input("Enter row number of product to save: "))
			if indx<len(self.df):
				if os.path.exists(self.user_list):
					old_data=pd.read_csv(self.user_list)
				else:
					old_data=pd.DataFrame()
				if self.df.title[indx] not in old_data:
					old_data=pd.concat([old_data,self.df.iloc[[indx]]])
					print(self.df.iloc[[indx]])
				old_data.to_csv(self.user_list, index=False,header=self.df.columns)

		pass

	def extract_list(self):
		pass

	def scrape(self,prod):
		products_1 = scraper.searchAmazon(prod,1)
		products_2 = scraper.searchWalmart(prod,1)
		products_3 = scraper.searchEtsy(prod,1)
		results=scraper.driver(prod,df_flag=1)
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
				print("Incorrect Option")

