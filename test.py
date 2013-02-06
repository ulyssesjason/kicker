import sys
import csv




def main():
	with open("export.csv","rb") as f:
		reader=csv.reader(f)
	
		for email,fname,mname,lname,title,company,wphone,hphone,address1,\
			address2,address3,city,state,other_state,country,zipcode,subzipcode,notes in reader:
			


if __name__ == '__main__':
	main()