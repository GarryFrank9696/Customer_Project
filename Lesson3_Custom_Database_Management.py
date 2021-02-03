import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="games"
)

mycursor = mydb.cursor()

def createTable():
    mycursor.execute("create table if not exists more_customers (id int auto_increment primary key, name varchar(255), address varchar(255))")

createTable()

def existsCustomers(name, address):
    query = "select count(*) from more_customers where name='{}'".format(name)
    print(query)
    mycursor.execute(query)
    
    myresult = mycursor.fetchall()
    
    
    print("myresluts=")
    print(myresult)
    print("myresult[0]=")
    print(myresult[0])
    print("myresult[0][0]")
    
    
    count = myresult[0][0]
    print(count)
    
    if count == 0:
        
        sql = "insert into more_customers (name, address) values (%s, %s)"
        val = (name, address)
        mycursor.execute(sql, val)
        
        mydb.commit()
        
        print(mycursor.rowcount, "records inserted.")
    else:
        print("Duplicate")
        
def menu():
    print("Type 'update' to update customers")
    print("Type 'add' to add customers")
    print("Type 'remove' to remove customers")
    print("Type 'quit' to end the process")

    choice = input("please insert the command you want to do: ")
    
    if choice == "quit":
        print("closed")
        
    elif choice== "update":
        update()
        choice= input("Enter 'back' to go back: ")
        
        if choice== "":
            menu()
            
    elif choice== "remove":
        remove()
        choice= input("Enter 'back' to go back: ")
        
        if choice== "back":
            menu()
    else:
        if choice== "add":
            add()
            choice= input("Enter 'back' to go back: ")
        
            if choice== "back":
                menu()

        


def add():
    answer = '' 
    while answer != "quit":
        answer = input("Please insert name of customr: ")
        if answer !=  "quit":
            name = answer
            address = input("Please insert address: ")
            existsCustomers(name, address)
            
def update():
    ID = input("Enter ID: ")
    name = input("Enter new name: ")
    address = input("Enter new address: ")
    sql = "UPDATE customers SET name = '{}', address = '{}' where id = '{}'".format(name, address, ID)
    mycursor.execute(sql)
    mydb.commit()
    print("Updated")
    
def remove():
    name = input("Enter name of the element you are removing: ")
    sql = "DELETE FROM customers where name = '{}'".format(name)
    mycursor.execute(sql)
    mydb.commit()
    print("Deleted")
    
menu()







    