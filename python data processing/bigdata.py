import pandas as pd 
import time
from sqlalchemy import create_engine, event, text
from pandas.io import sql

df = pd.read_csv (r'C:\Users\mdjos\workspaces\financial_transaction_analyzer\dataset\PS_20174392719_1491204439457_log.csv',
                  dtype={'step': float,
                         'type': str,
                         'amount': float,
                         'nameOrig': str,
                         'oldbalanceOrg': float,
                         'newbalanceOrig': float,
                         'nameDest': str,
                         'oldbalanceDest': float,
                         'newbalanceDest': float,
                         'isFraud': bool,
                         'isFlaggedFraud': bool})

print ("File read...")

df.dropna()

size = 2000000

list_of_dfs = [df.loc[i:i+size-1,:] for i in range(0, len(df),size)]

print ("File cleaned and split...")

engine = create_engine("mysql://[user]:[password]@localhost:3308/transactiondb?charset=utf8&local_infile=1")

connection = engine.connect()

try:
    tic = time.perf_counter()
    
    connection.execute("TRUNCATE TABLE transactions")
    
    print ("Table cleared...")
   
    for i in list_of_dfs:
        
        sql.to_sql(i, 
                   con=connection, 
                   name='transactions', 
                   schema='transactiondb', 
                   if_exists='append',
                   method=None,
                   chunksize=2000)
        print ("Finished a group...")
    
    toc = time.perf_counter()
    
except Exception as e:
    print (e)
        
print (toc - tic)
print ('done....')
connection.close()