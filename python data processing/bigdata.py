import pandas as pd 
from sqlalchemy import create_engine
from pandas.io import sql

df = pd.read_csv (r'C:\Users\mdjos\workspaces\financial_transaction_analyzer\dataset\test_data.csv')

print (df)

engine = create_engine("mysql://[user]:[password]@localhost:3308/transactiondb")

connection = engine.connect()
        
sql.to_sql(df, con=connection, name='transactions', schema='transactiondb', if_exists='replace')
        
connection.close()