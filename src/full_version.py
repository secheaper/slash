import json
import os

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





	def driver(self):
		self.login()
		print("Welcome ",self.name)
