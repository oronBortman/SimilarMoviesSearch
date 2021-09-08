from utils.create_db_functions import CreateDB
from utils.import_json_to_db_functions import *


if __name__ == '__main__':
    CreateDB().start()
    ImportJsonToDB().start()


