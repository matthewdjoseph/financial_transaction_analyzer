import pandas as pd 
import mysql.connector
from mysql.connector import Error

df = pd.read_csv (r'C:\Users\mdjos\workspaces\financial_transaction_analyzer\dataset\PS_20174392719_1491204439457_log.csv')

print (df)

connection = mysql.connector.connect(host='localhost',
                                     database='transactiondb',
                                     user=[user],
                                     password=[password],
                                     port='3308')
        
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
connection.close()