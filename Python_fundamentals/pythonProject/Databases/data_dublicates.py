import pandas as pd
import mysql.connector
from main import mydb
# Read sqlite query results into a pandas DataFrame
def clean_data():

    con = mydb


    df = pd.read_sql_query("SELECT * FROM names_and_adress.customers ORDER BY name;", con)
    #order database Frame by name
    df = df.drop_duplicates(subset=["name", "address"], keep='first')
    #clean the database by some column names

    mydb.commit()
    con.close()
    return  print(df)


clean_data()