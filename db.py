import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="ndovu",
    password="Password-13",
    database="pythonusers",
)

dbcursor = db.cursor()
# dbcursor.execute("CREATE DATABASE pythonusers")