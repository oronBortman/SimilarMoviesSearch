import mysql.connector as mysql

from settings.configuration import DB_NAME
from variables import globals_variables


def sql_execute(query):
    if globals_variables.cursor:
        use_db(DB_NAME)
        globals_variables.cursor.execute(query)
    globals_variables.db.commit()


def sql_exec_ret_first_elem(query):
    res = sql_execute_ret(query)
    if res:
        return res[0][0]
    else:
        return None


def sql_execute_ret(query):
    if globals_variables.cursor:
        globals_variables.cursor.execute(query)
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
