from settings.configuration import *
from utils.general_db_functions import *
from variables import globals_variables

class ActionsOnDB:

    def operation_on_db(self):
        pass

    def start(self) -> None:
        try:
            globals_variables.db = create_db_connection(HOSTNAME, DB_USER, DB_PASSWD)
            globals_variables.cursor = globals_variables.db.cursor(buffered=True)
            self.operation_on_db()
            globals_variables.db.commit()
        except Exception as error:
            print(error)
        finally:
            globals_variables.cursor.close()
            globals_variables.db.close()
