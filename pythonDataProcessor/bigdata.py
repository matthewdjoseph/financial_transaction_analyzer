import pandas as pd 
import time
from sqlalchemy import create_engine, event, text
from pandas.io import sql

engine = create_engine("mysql+mysqlconnector://root:Fu7ur388!@localhost:3308/transactiondb?charset=utf8")

def do_remove():
    
    connection = engine.connect()
    
    try:
        connection.execute("TRUNCATE TABLE transactions")

        print ("Table cleared...")

    except Exception as e:
        print (e)

    print ('done....')
    connection.close()

def do_process():
    df = pd.read_csv (r'C:\Users\mdjos\workspaces\financial_transaction_analyzer\dataset\test_data.csv',
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
                       chunksize=2000)
            print ("Finished a group...")

    except Exception as e:
        print (e)

    print ('done....')
    connection.close()

if __name__ == '__main__':
    do_process()