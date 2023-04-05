import os
import mysql.connector
import pandas as pd
import csv




def fetch_themes(idb, url):
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
    mycursor.execute(f"SELECT url FROM user_info WHERE id = {idb}")
    result = mycursor.fetchall()
    if len(result) > 0:
        for r in result:
            url = r
        return url 
    
    else:
        mycursor.execute(f"INSERT into user_info VALUES({idb}, \"{url}\")")
        mydb.commit()
        mydb.close()
        return url
    

print(fetch_themes(4, "lol/dsadas/aaasda"))
