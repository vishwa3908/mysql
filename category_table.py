import mysql.connector
from shopping_category import *
from customer_category import *
from customer_shopping import *
from tabulate import tabulate




def create_category_table(category_table_name):
	mydb = mysql.connector.connect(
    host="localhost",
    user="vishwa",
    password="Password.123",
    database = "shopping"
    )
	mycursor = mydb.cursor()
	create_category_table_query = '''CREATE TABLE IF NOT EXISTS {}(ID INT AUTO_INCREMENT PRIMARY KEY,ITEMS VARCHAR(20),PRICE INT )'''.format(category_table_name)
	mycursor.execute(create_category_table_query)


	def inserting_into_subtable(sub_table):
		print("------------Enter into Sub Table----------------- ")
		subtable_data = input("Enter Sub Table data => " ).capitalize()
		subtable_data_price = input("Enter {} Price => ".format(subtable_data))
		subtable_value = (subtable_data,subtable_data_price)
		inserting_into_subtable_query = '''INSERT INTO {}(ITEMS,PRICE)VALUES(%s,%s)'''.format(sub_table)
		mycursor.execute(inserting_into_subtable_query,subtable_value)
		mydb.commit()

	subtable_choice = input("You want to add in {} Y/N => ".format(category_table_name)).capitalize()
	if subtable_choice=="Y":

		inserting_into_subtable(category_table_name)
	else:
		pass


def show_subtable(category_table_name):
	try:
		mydb = mysql.connector.connect(
	    host="localhost",
	    user="vishwa",
	    password="Password.123",
	    database = "shopping"
	    )
		mycursor = mydb.cursor()
		mycursor.execute('''SELECT * FROM {}'''.format(category_table_name))
		sub_table_result = mycursor.fetchall()
		if sub_table_result:
			header = ["ID","{}Type".format(category_table_name),"Cost"]
			print(tabulate(sub_table_result,headers = header,tablefmt ='fancy_grid',stralign='center'))
			buying_choice = input("Do you want anything from this category? Y/N => ").upper()
			if buying_choice !="Y":
				return
			elif buying_choice == "Y":
				buying_item = input("Enter Item You Want To buy => ").capitalize()
				shopping_cart(category_table_name,buying_item)
		else:
			print("Nothing Found !!!")
	except:
		print("Invalid category")


def delete_from_subtable(category_table_name,delete_sub_table_data):
	mydb = mysql.connector.connect(
    host="localhost",
    user="vishwa",
    password="Password.123",
    database = "shopping"
    )
	mycursor = mydb.cursor()
	delete_sub_table_data_val = (delete_sub_table_data,)
	delete_sub_table_data_query = '''DELETE FROM {} WHERE ITEMS = %s'''.format(category_table_name)
	mycursor.execute(delete_sub_table_data_query,delete_sub_table_data_val)
	mydb.commit()
	print("{} Deleted".format(delete_sub_table_data))



def add_into_subtable(category_table_name):
	mydb = mysql.connector.connect(
    host="localhost",
    user="vishwa",
    password="Password.123",
    database = "shopping"
    )
	mycursor = mydb.cursor()
	adding_amount = int(input("How many items you want to add ? => "))
	for i in range(adding_amount):
		new_subdata = input("Enter Item => ").capitalize()
		new_subdata_price = int(input("Enter {} Price => ".format(new_subdata)))
		adding_subdata_value = (new_subdata,new_subdata_price)
		adding_subdata_query = ''' INSERT INTO {}(ITEMS,PRICE)VALUES(%s,%s)'''.format(category_table_name)
		mycursor.execute(adding_subdata_query,adding_subdata_value)
		mydb.commit()
		print("{} Inserted".format(new_subdata))
