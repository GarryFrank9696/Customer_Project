import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="games"
)

mycursor = mydb.cursor()

def createTable():
    mycursor.execute("create table if not exists customers (id int auto_increment primary key, name varchar(255), address varchar(255))")

createTable()

def insertCustomer(name, address):
    sql = "insert into customers (name, address) values (%s, %s)"
    val = (name, address)
    mycursor.execute(sql, val)
    
    mydb.commit()
    
    print(mycursor.rowcount, "records inserted.")
    
insertCustomer("John", "Highway 21")