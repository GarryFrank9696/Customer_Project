import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="games"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)
    
query = "select * from gamz limit 5;"

mycursor.execute(query)

myresult = mycursor.fetchall()

for row in myresult:
    print(row)


