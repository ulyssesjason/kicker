import sys
import csv
import data 
import sqlite3 as lite

def 



def main():
	with open("export.csv","rb") as f:
		reader=csv.reader(f)
		
		for email,fname,mname,lname,title,company,wphone,hphone,address1,\
			address2,address3,city,state,other_state,country,zipcode,sub_zipcode,notes in reader:
			


if __name__ == '__main__':
	main()