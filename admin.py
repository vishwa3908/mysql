# Creating admin view
import mysql.connector
from shopping_category import *
from category_table import *
from customer_shopping import *
from tabulate import tabulate


def admin_view():
	mydb = mysql.connector.connect(
  	host="localhost",
  	user="vishwa",
  	password="Password.123",
  	database = "shopping")
	print('''
  			What Records You want to see\n
  			1. Customer Records   2. Category Items  3.Quit

  		''')
	admin_choice = int(input("Enter Your Choice => "))



# Showing Customer Records---------------------------------------------------------------

	def customer_records():

		mycursor = mydb.cursor()
		mycursor.execute('''SELECT NAME,AGE,GENDER FROM customers''')
		admin_result = mycursor.fetchall()
		if admin_result:
			customer_list = []
			print("Welcome Admin !!")
			header = ['Name',"Age","Gender"]
			print(tabulate(admin_result,headers = header,tablefmt ='fancy_grid',stralign='center'))
			for i in admin_result:
		  		customer_list.append(i)
			
			for data in range(len(customer_list)):
				show_total_customer_cart(customer_list[data][0])
			admin_view()
		else:
			print("No Category Found")
			admin_view()











	def quit():
		return



	if admin_choice == 1:
		customer_records()
	elif admin_choice ==2:
		category()
	elif admin_choice==3:
		quit()