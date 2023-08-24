import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd ='cgea@ISIA2023'
)

# prepare a cursor objet
cursorObject = dataBase.cursor()


#create a database
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done AuthentiK!")

