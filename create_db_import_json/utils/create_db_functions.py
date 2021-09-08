from utils.create_table_functions import *
from utils.action_on_db import *


class CreateDB(ActionsOnDB):
    def __create_db(self, db_name):
        query = f'CREATE DATABASE {db_name};'
        if globals_variables.cursor:
            globals_variables.cursor.execute(query)

    def __drop_db(self, db_name):
        query = f'DROP DATABASE if exists {db_name};'
        if globals_variables.cursor:
            globals_variables.cursor.execute(query)


    def operation_on_db(self) -> None:
        self.__drop_db(DB_NAME)
        self.__create_db(DB_NAME)
        create_movies_table()
        create_categories_tables()
