import mysql.connector
from welcome import *
from customer import *
from shopping_category import *









mydb = mysql.connector.connect(
  host="localhost",
  user="vishwa",
  password="Password.123",
  database = "shopping"
 )
welcome()
choice()