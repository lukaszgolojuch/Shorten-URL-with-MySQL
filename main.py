import mysql.connector
import os
import sys

# Name: Shorten URL
# Language: Python
# Environment: Visual Studio Code
#
# Author Lukasz Golojuch

#config mysqlDB if you not have db config yet open config.py 
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Password123$",
database="urls"
)

def search():

    print("--------------------------------------------")
    print("Short url: ")
    #Input your url you are looking for
    short_url = "www.shorturl.com/"
    short_url = short_url +  raw_input("www.shorturl.com/")
    
    mycursor = mydb.cursor()

    #Search for shortpage name in our DB
    sql = "SELECT pages FROM customers WHERE shortpages = %s"
    adr = (short_url, )

    mycursor.execute(sql, adr)  

    myresult = mycursor.fetchall()

    print(myresult[0])

def new_website():

    print("--------------------------------------------")
    print("Original url: ")
    #Input original URL
    original_url = raw_input()
    print("Short url: ")
    short_url = "www.shorturl.com/"
    #Input only suffix of short url
    short_url = short_url + raw_input("www.shorturl.com/")

    mycursor = mydb.cursor()
        
    #Insert our new website to DB
    sql = "INSERT INTO customers (pages, shortpages) VALUES (%s, %s)"
    val = (original_url, short_url)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def main():
    print("================================")
    print("Hello", os.getlogin())
    print("Menu:")
    print("1. Search")
    print("2. Add new website")
    print("3. Exit")

    odp = input("Your choice: ")

    if odp == 1:
        #Search for your website
        search()
    elif odp == 2: 
        #Input new website
        new_website()
    elif odp == 3:
        #Turn off app
        sys.exit("Thank you for using my application")
    else:
        #Wrong input
        print("Wrong input...")
        print("Try again...")

if __name__ == '__main__':
    main()

