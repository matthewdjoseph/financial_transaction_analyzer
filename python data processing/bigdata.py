import pandas as pd 
from sqlalchemy import create_engine, event
from pandas.io import sql

df = pd.read_csv (r'C:\Users\mdjos\workspaces\financial_transaction_analyzer\dataset\PS_20174392719_1491204439457_log.csv')

print ("File read...")

size = 500000

list_of_dfs = [df.loc[i:i+size-1,:] for i in range(0, len(df),size)]

print ("File split...")

engine = create_engine("mysql://[user]:[password]@localhost:3308/transactiondb")

connection = engine.connect()

try:
    connection.execute("TRUNCATE TABLE transactions")
    
    print ("Table cleared...")
    
    for i in list_of_dfs:
        sql.to_sql(i, 
                   con=connection, 
                   name='transactions', 
                   schema='transactiondb', 
                   if_exists='append',
                   method=None,
                   chunksize=10000)
        print ("Finished a group...")
    
except Exception as e:
    print (e)
        
print ('done....')
connection.close()