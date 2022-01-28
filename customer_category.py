from shopping_category import *
from category_table import *
import mysql.connector
from tabulate import tabulate







def customer_category():
	mydb = mysql.connector.connect(
    host="localhost",
    user="vishwa",
    password="Password.123",
    database = "shopping"
    )
	mycursor = mydb.cursor()
	print("Which Category you Want to Shop ?")
	def show_customer_category():
		mycursor.execute("SELECT * FROM category")
		show_category_result = mycursor.fetchall()
		count = 1
		if show_category_result:
			print("----Categories----")
			print(tabulate(show_category_result,tablefmt ='fancy_grid',stralign='center'))
			
			customer_sub_category_choice = input("Enter Sub Category you want to explore => ").capitalize()
			show_subtable(customer_sub_category_choice)





			

		else:
			print("No Category Found")




	show_customer_category()


