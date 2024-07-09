# sql.py
import sqlite3
from langchain_core.tools import Tool
from typing import List
from pydantic.v1 import BaseModel

connection = sqlite3.connect("db.sqlite")

def tables_str():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("Select name from sqlite_master where type = 'table'")
    tables = cursor.fetchall()
    return '\n'.join(row[0] for row in tables if row[0] != None)
    
def run_sqlite_query(query):
    cursor = connection.cursor()
    try:# Error Handling
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.OperationalError as err:
        return f'The following error occurred: {str(err)}'

# By making this class, we have created some kind of record inside of our program. It says essentially, if you want to be a class of RunQueryArgsSchema, you must provide a 'query' attribute that is a string. We then provided that off to our tool under the keyword argument args_schema. Langchain internally is going to use this information to better describe the different arguments that ChatGPT should be providing to our tool. So in this case, it's gonna tell ChatGPT, "Okay, if you want to make use of this tool and if you want to use this function, you must provide an argument called query, and it's supposed to be a string."
class RunQueryArgsSchema(BaseModel):
    query: str

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run a SQLite query.",
    func=run_sqlite_query
)

def describe_tables(table_names):
    # tables_list = table_names.split('\n')    # This is not required if you define a Pydantic class DescribeTablesArgsSchema
    tables = "('" + "', '".join(table_names) + "')"
    cursor = connection.cursor()
    rows = cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' and name IN {tables};")
    return '\n'.join(row[0] for row in rows if row[0] is not None)

class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]
    
describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, returns the schema of those tables",
    func=describe_tables,
    args_schema=DescribeTablesArgsSchema
)