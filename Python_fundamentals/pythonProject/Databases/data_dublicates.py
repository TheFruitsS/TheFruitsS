


import pandas as pd


from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/names_and_adress')


def clean_data():

    connection = engine.connect()


    df = pd.read_sql_query("SELECT * FROM customers_test ORDER BY name;", connection)
    print(df)
    #order database Frame by name
    #clean = df.drop_duplicates(subset=["name", "address"], keep='first')


    #clean1 = clean.to_sql('customers_test',connection ,if_exists='replace')



    return



clean_data()