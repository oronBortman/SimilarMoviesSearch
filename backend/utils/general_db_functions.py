import mysql.connector as mysql
from global_variables import globals_variables
from settings.configuration import *


def sql_execute_ret(query):
    if globals_variables.cursor:
        use_db(DB_NAME)
        for result in globals_variables.cursor.execute(query, multi=True):
            if result.with_rows:
                return result.fetchall()
        return globals_variables.cursor.fetchall()
    else:
        return None


def create_db_connection(host, user, passwd):
    database = mysql.connect(
        host=host,
        user=user,
        passwd=passwd, # need to add encrypted connection
    )
    return database


def use_db(db_name):
    query = f'USE {db_name};'
    globals_variables.cursor.execute(query)
