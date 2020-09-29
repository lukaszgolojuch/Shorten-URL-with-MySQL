import mysql.connector
import os
import sys

# Name: Shorten URL
# Language: Python
# Environment: Visual Studio Code
#
# Author Lukasz Golojuch

def config():
    
    host_input = raw_input("Host: ")
    user_input = raw_input("User: ")
    password_input = raw_input("Password: ")
    
    #inicialize DB 
    mydb = mysql.connector.connect(
    host=host_input,
    user=user_input,
    password=password_input
    )

    mycursor = mydb.cursor()
    #Create DB named urls 
    mycursor.execute("CREATE DATABASE urls")

    #inicialize DB once again with database name
    mydb = mysql.connector.connect(
    host=host_input,
    user=user_input,
    password=password_input,
    database="urls"
    )

    mycursor = mydb.cursor()
    #Create tables pages and short_pages
    mycursor.execute("CREATE TABLE customers (pages VARCHAR(255), shortpages VARCHAR(255))")
    #Create auto increment primary key
    mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

    print("Configuration finished")
    #Now you have to change couple things in main.py
    print("--------------------------------")
    print("Now go to main.py and change: ")
    print("host = ", host_input)
    print("user = ", user_input)
    print("password = ", password_input)
    print("--------------------------------")
    print("Now you can use main application")
    sys.exit("Good job!!")

def main():
    print("================================")
    print("Do you want to config your DB?")
    print("Y/N")
    answ = raw_input()
    if answ == "Y" or answ == "y":
        #START configuration
        config()
    elif answ == "N" or answ == "n":
        #Turn down program 
        sys.exit("Thank you for using my application")
    else:
        print("Wrong input...")
        main()

if __name__ == '__main__':
    print("Hello", os.getlogin())
    main()