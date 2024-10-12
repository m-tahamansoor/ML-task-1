import mysql.connector 

DataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mansoor",
    database = "sakila"
)

if DataBase.is_connected():
    print("Succesfully connected!")
else:
    print("Not Connected!")

cursor = DataBase.cursor()

query = "Select * from actor"

cursor.execute(query)

result = cursor.fetchall()

for rows in result:
    print(rows)