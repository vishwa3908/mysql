# from shopping_category import *
import mysql.connector
from customer_category import *
from category_table import * 
from customer_shopping import *











# CREATE CUSTOMER TABLE IF NOT ALREADY  PRESENT--------------------------

def customer_table():
  mydb = mysql.connector.connect(
  host="localhost",
  user="vishwa",
  password="Password.123",
  database = "shopping"
 )
  mycursor = mydb.cursor()

  mycursor.execute('''CREATE TABLE IF NOT EXISTS customers(NAME VARCHAR(30) PRIMARY KEY,AGE INT,GENDER VARCHAR(10),PASSWORD VARCHAR(20))''')

# Asking Customer Details--------------------------------------------

  check  = input("Are You a new Customer ? (Y/N) => ")
  if check.upper() == "Y":
    customer_name = input("Enter Your Name => ")
    customer_age = int(input("Enter Your Age => "))
    customer_gender = input("Enter Your Gender (M/F) => ")

    def password_entry():

      customer_password = input("Enter Password => ")
      customer_confirm_password = input("Confirm Your Password => ")

# Confirming Password--------------------------------------------------------

      if customer_password == customer_confirm_password:
        val = (customer_name.capitalize(),customer_age,customer_gender.upper(),customer_password)
        sql = ''' INSERT INTO customers(NAME,AGE,GENDER,PASSWORD)VALUES(%s,%s,%s,%s)'''

        mycursor.execute(sql,val)
        mydb.commit()

        print(mycursor.rowcount, "Record Inserted")

# Shopping Function Called------------------------------------------

        customer_start_shopping(customer_name.capitalize())


        customer_category()


      else:

        print("Password Does not Match ")

# Re-attempt for password entry--------------------------

        password_entry()

    password_entry()

# Checking Old customer records------------------------

  elif check.upper()=="N":

    check_customer = input("Enter Your Name => ").capitalize()
    old_customer_password = input("Enter Your Password => ")
    val = (check_customer,old_customer_password,)
    sql = "SELECT NAME,AGE,GENDER FROM customers where NAME = %s and PASSWORD = %s"

    mycursor.execute(sql,val)
    result = mycursor.fetchall()

# If Credential Matched-----------------------------------------

    if result:
      for i in result:
        print(i)
        print("Logged In Successfully")
        showing_cart_choice = input("You Want to see your Cart Y/N => ").upper()
        if showing_cart_choice == "Y":
          show_total_customer_cart(check_customer)
          updating_cart_choice = input(" Do You want to Remove Item Y/N => ").upper()
          if updating_cart_choice == "Y":
            delete_item_data = input("Enter Item You Want to Delete => ").capitalize()
            update_customer_cart(check_customer,delete_item_data)
          

          customer_category()
        elif showing_cart_choice =="N":
          customer_category()
        else:
          print("Wrong Choice")
          customer_category()
        customer_category()
    else:
      print("Credential Does not Match")

# If credential does not matched password updating is done --------------------------------

      def update_password():
          
          password_reset_choice = input("Do you Want to reset your password (Y/N) => ").upper()

          if password_reset_choice == "Y":

            customer_new_password = input("Enter Your New Password => ")
            customer_confirm_new_password = input("Confirm Your Password => ")

            if customer_new_password == customer_confirm_new_password:

              password_value = (customer_new_password,check_customer)
              password_update_query = '''UPDATE customers SET PASSWORD = %s WHERE NAME = %s'''
              mycursor.execute(password_update_query,password_value)
              mydb.commit()

              print("Password Updated")
              customer_table()
          else:

            customer_table()
      update_password()

  else:
    print("      Wrong Choice \n Please Enter right choice!!")
    customer_table()
