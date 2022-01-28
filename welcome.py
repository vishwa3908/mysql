from customer import *
from admin import *
from shopping_category import *


def welcome():
	print('''\n\n\t\t\t\t\t\t-----------------Welcome To Shopbuddy----------------------''')


def choice():
	print('''\n\n\n\t\t\t\t\t------------- 1. Customer\t2. Merchant\t3. Admin--------------\n\n''')     
	choice_entered = int(input("Enter Your Choice => "))
	if choice_entered == 1:
		customer_table()
	elif choice_entered == 3:
		admin_view()
	elif choice_entered ==2:
		print("Facility not availale at this Moment")
		return

