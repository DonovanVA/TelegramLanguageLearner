import pandas as pd
from sqlalchemy import create_engine
import json
def queryDB(query, url):
    """
    Executes a SQL query on a database and returns the result as a pandas DataFrame.

    Parameters:
    query (str): The SQL query to be executed.
    url (str): The URL or connection string for the database.

    Returns:
    pandas.DataFrame: The result of the query as a DataFrame.
    """
    engine = create_engine(url)
    out_df = pd.read_sql(query, engine)
    print(out_df)
    return out_df

def createReplaceDB(df, table_name, url):
    """
    Creates a new table in the database if it does not already exist and inserts the data from a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to be inserted.
    table_name (str): The name of the table to be created.
    url (str): The URL or connection string for the database.

    Returns:
    None
    """
    engine = create_engine(url)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def AppendDB(df, table_name, url):
    """
    Appends data from a DataFrame to an existing table in the database.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to be appended.
    table_name (str): The name of the table to append the data to.
    url (str): The URL or connection string for the database.

    Returns:
    None
    """
    engine = create_engine(url)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

def queryCSV(filepath):
    """
    Reads a CSV file and returns the data as a pandas DataFrame.

    Parameters:
    filepath (str): The path to the CSV file.

    Returns:
    pandas.DataFrame: The data from the CSV file as a DataFrame.
    """
    out_df = pd.read_csv(filepath)
    return out_df

def createReplaceCSV(df, filepath):
    """
    Creates a new CSV file or replaces an existing one with the data from a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to be saved.
    filepath (str): The path to the CSV file.

    Returns:
    None
    """
    df.to_csv(filepath,sep=",",index=False)

# Read the JSON file
def jsonToDict(filepath):
    """
    Reads a JSON file and returns the data as a Python dictionary.

    Parameters:
    filepath (str): The path to the JSON file.

    Returns:
    dict: The data from the JSON file as a Python dictionary.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        json_data = file.read()

    # Convert JSON data to a Python dictionary
    dict_data = json.loads(json_data)
    return dict_data

