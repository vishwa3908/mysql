import mysql.connector
from tabulate import tabulate
from customer_category import *







def customer_start_shopping(customer_name):
	mydb = mysql.connector.connect(
  	host="localhost",
  	user="vishwa",
  	password="Password.123",
  	database = "shopping"
 	)
	mycursor = mydb.cursor()
	creating_customer_shopping_table_query = '''CREATE TABLE IF NOT EXISTS {}(ITEM_TYPE VARCHAR(20) , ITEM VARCHAR(33) ,PRICE INT)'''.format(customer_name)
	mycursor.execute(creating_customer_shopping_table_query)





def shopping_cart(category_name,buying_item):
	mydb = mysql.connector.connect(
  	host="localhost",
  	user="vishwa",
  	password="Password.123",
  	database = "shopping"
 	)
	mycursor = mydb.cursor()
	customer_name = input("Enter Your Name Again => ").capitalize()
	buying_item_price_val = (buying_item,)
	buying_item_price_query = '''SELECT PRICE FROM {} WHERE ITEMS = %s'''.format(category_name)
	mycursor.execute(buying_item_price_query,buying_item_price_val)
	buying_item_price_query_result = mycursor.fetchall()
	price_of_item = buying_item_price_query_result[0][0]
	customer_personal_cart_val = (category_name,buying_item,price_of_item)
	customer_personal_cart_query = '''INSERT INTO {}(ITEM_TYPE,ITEM,PRICE)VALUES(%s,%s,%s)'''.format(customer_name)
	mycursor.execute(customer_personal_cart_query,customer_personal_cart_val)
	print("Added to cart successfully !!")
	mydb.commit()


def show_total_customer_cart(customer_name):
	mydb = mysql.connector.connect(
  	host="localhost",
  	user="vishwa",
  	password="Password.123",
  	database = "shopping"
 	)
	mycursor = mydb.cursor()
	show_total_customer_cart_query = '''SELECT * FROM {}'''.format(customer_name)
	mycursor.execute(show_total_customer_cart_query)
	show_total_customer_cart_result = mycursor.fetchall()
	if show_total_customer_cart_result:
		header = ["Item Type", "Item","Price"]
		print("\n\n {}".format(customer_name))
		print(tabulate(show_total_customer_cart_result,headers = header,tablefmt ='fancy_grid',stralign='center'))

		total_cart_value_query = '''SELECT SUM(PRICE) FROM {}'''.format(customer_name)
		mycursor.execute(total_cart_value_query)
		total_cart_result  = mycursor.fetchall()
		print("Total Cart Value => ",total_cart_result[0][0])
		print("\n")


def update_customer_cart(customer_name,delete_item):
	mydb = mysql.connector.connect(
  	host="localhost",
  	user="vishwa",
  	password="Password.123",
  	database = "shopping"
 	)
	mycursor = mydb.cursor()
	update_customer_cart_val = (delete_item,)
	update_customer_cart_query = '''DELETE FROM {} WHERE ITEM = %s'''.format(customer_name)
	mycursor.execute(update_customer_cart_query,update_customer_cart_val)
	mydb.commit()
	show_total_customer_cart(customer_name)
