from settings.configuration import *
from utils.general_db_functions import *


def create_movies_table():
    query = '''
    CREATE TABLE movies (
        id BIGINT NOT NULL AUTO_INCREMENT,
        title VARCHAR(100) NOT NULL, 
        release_date VARCHAR(40),
        movie_box_office_revenue BIGINT,
        plot_summary text NOT NULL,
        feature_length BIGINT,
        PRIMARY KEY(id)
    );'''
    sql_execute(query)


def create_category_tables(singular, category_table_name):
    create_category_table(category_table_name)
    create_movies_category_table(singular, category_table_name)


def create_category_table(category_table_name):
    query = f'''
    CREATE TABLE {category_table_name}(
        id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(40) UNIQUE NOT NULL
    );'''
    sql_execute(query)


def create_movies_category_table(singular, category_table_name):
    category_id = f"{singular}_id"
    table_name = f"movies_{category_table_name}"

    query = f'''
    CREATE TABLE {table_name}(
        {MOVIE_ID} BIGINT NOT NULL,
        {category_id} BIGINT NOT NULL,
        FOREIGN KEY ({MOVIE_ID}) REFERENCES movies (id) ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY ({category_id}) REFERENCES {category_table_name} (id) ON DELETE RESTRICT ON UPDATE CASCADE,
        PRIMARY KEY ({MOVIE_ID}, {category_id})
    );'''
    sql_execute(query)


def create_categories_tables():
    for singular, plural, _ in MOVIE_CATEGORIES:
        create_category_tables(singular, plural)

