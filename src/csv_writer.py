import csv
from datetime import datetime
import os


def write_csv(arr,product,file_path):
	os.chdir(file_path)
	keys = arr[0].keys()
	now=datetime.now()
	file_name=product+now.strftime("%m%d%y_%H%M")+'.csv'
	a_file = open(file_name, "w", newline='')
	dict_writer = csv.DictWriter(a_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(arr)
	a_file.close()