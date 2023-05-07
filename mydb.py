# Install MySQL from website
# pip istall mysql
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

# prepare a cursor object for the database
cursorObject = dataBase.cursor()

#create a databse
cursorObject.execute("CREATE DATABASE elderco")

print("Database created!")