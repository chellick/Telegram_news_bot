import os
import mysql.connector
import pandas as pd
import csv


def connect_mysql():
    file_p = os.path.join('C:/Users/Matvey/OneDrive/Рабочий стол/sqltoken.txt')

    with open(file_p, 'r') as f:
        password = f.read()
        
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="telegram_test_bot"
    )

    mycursor = mydb.cursor()
    print('DB connected')
    return mycursor, mydb




def fetch_themes(id, url):
    file_p = os.path.join('C:/Users/Matvey/OneDrive/Рабочий стол/sqltoken.txt')

    with open(file_p, 'r') as f:
        password = f.read()
        
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="telegram_test_bot"
    )

    mycursor = mydb.cursor()
    print('DB connected')


    mycursor.execute(f"INSERT into user_info VALUES({id}, {url})")
    mydb.commit()
    return print('FETCHED THEMES')

print(fetch_themes(1, 'test/url'))




