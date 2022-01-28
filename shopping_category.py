# CREATING SHOPPING MENU FOR CUSTOMERS------------------------------------
from category_table import *
import mysql.connector
from tabulate import tabulate
from customer_shopping import *



def category():
	mydb = mysql.connector.connect(
		host="localhost",
		user="vishwa",
		password="Password.123",
		database = "shopping")
	mycursor = mydb.cursor()
	mycursor.execute('''CREATE TABLE IF NOT EXISTS category(CATEGORY_NUMBER INT AUTO_INCREMENT PRIMARY KEY, CATEGORY_NAME VARCHAR(20))''')

# Show all categories present ---------------------------------

	def show_category():
		mycursor.execute("select * from category")
		show_category_result = mycursor.fetchall()
		count = 1
		if show_category_result:
			print("----Categories----")
			header = ["Id","Category"]
			print(tabulate(show_category_result,headers = header,tablefmt ='fancy_grid',stralign='center'))

# Exploring Sub category ---------------------------------------------------

			entering_sub_category_choice = input("Do You Want to Explore Sub Category Y/N => ").capitalize()

			if entering_sub_category_choice =="Y":

				sub_category_admin_choice = input("Which Sub Category you Want to Enter => ").capitalize()
				sub_category_admin_choice_query = "SELECT * FROM {}".format(sub_category_admin_choice)
				mycursor.execute(sub_category_admin_choice_query)
				sub_category_admin_result = mycursor.fetchall()
				admin_sub_count = 1
				if sub_category_admin_result:
					header = ["ID","{} Type".format(sub_category_admin_choice),"Cost"]
					print(tabulate(sub_category_admin_result,headers= header,tablefmt ='fancy_grid',stralign='center'))
					delete_sub_category_item_choice = input("Do you want to delete any item Y/N => ").upper()
					if delete_sub_category_item_choice == "Y":
						delete_sub_category_item = input("Enter Item you want to delete => ").capitalize()
						delete_from_subtable(sub_category_admin_choice,delete_sub_category_item)
					else:
						adding_choice = input("Do You want to add items ? Y/N => ").upper()
						if adding_choice == "Y":
							add_into_subtable(sub_category_admin_choice)
				else:

					print("No Sub Category Found")
		else:
			print("No Category Found")

# Adding new Category ---------------------------------------------

	def add_category():
		category_input_data = input("Enter Category = > ").capitalize()
		category_data =category_input_data
		category_val = (category_data,category_data)
		category_sql = '''INSERT INTO category(CATEGORY_NAME)SELECT * FROM(SELECT %s) as temp WHERE NOT EXISTS(SELECT CATEGORY_NAME FROM category WHERE CATEGORY_NAME = %s)LIMIT 1''' 
		mycursor.execute(category_sql,category_val)
		mydb.commit()
		create_category_table(category_data)

		category()


	


# Deleting Category -------------------------------------------------

	def delete_category():
		delete_category_input = input("Enter Category You want to delete => ").capitalize()
		delete_category_query = '''DROP TABLE IF EXISTS {}'''.format(delete_category_input)
		mycursor.execute(delete_category_query)
		removing_value = (delete_category_input,)
		removing_from_category_query = '''DELETE FROM category WHERE CATEGORY_NAME = %s'''
		mycursor.execute(removing_from_category_query,removing_value)
		mydb.commit()
		print("{} Deleted".format(delete_category_input))
		category()

# Updating Category ---------------------------------------------------

	def update_category():
		show_category()
		update_category_input = input("Enter Category you want to update => ").capitalize()
		updated_category_input = input("Enter New Category => ").capitalize()
		update_category_value = (updated_category_input,update_category_input)
		update_category_query = ''' update category set CATEGORY_NAME = %s WHERE CATEGORY_NAME = %s'''
		mycursor.execute(update_category_query,update_category_value)
		mydb.commit()
		show_category()







	def quit():
		return
	
	def admin_category_choice():
		admin_category_input = int(input("Your Choice => "))
		if admin_category_input == 1:

			add_category()
		elif admin_category_input == 2:
			show_category()
			category()
		elif admin_category_input==3:
			delete_category()
		elif admin_category_input==4:
			update_category()

		elif admin_category_input == 5:
			quit()
		else:
			print("Wrong Input ")
			admin_category_choice()	
	print('''What do you want to see
			1. Add Category   2. Show Category   3.Delete Category  4.Update Category   5.Quit''')

		
	admin_category_choice()
