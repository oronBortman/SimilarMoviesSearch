from utils.general_db_functions import *


def insert_movie_to_movies_table(title, release_date, movie_box_office_revenue, plot_summary, feature_length):
    query = f'''
    INSERT INTO movies (title, release_date, movie_box_office_revenue, plot_summary, feature_length) 
    VALUES ({title}, {release_date}, {movie_box_office_revenue} , {plot_summary}, {feature_length});
    '''
    print(query)
    sql_execute(query)
    query = f'SELECT max(id) FROM movies'
    return sql_exec_ret_first_elem(query)


def check_if_category_exists(category_table, category_val):
    query = f"SELECT EXISTS(SELECT * from {category_table} WHERE name=\"{category_val}\");"
    if sql_exec_ret_first_elem(query) == 1:
        return True
    else:
        return False


def insert_category_val(category_table, category_val):
    query = f"INSERT INTO {category_table} (name) VALUES (\"{category_val}\");"
    print(query)
    sql_execute(query)


def get_category_id(category_table, category_val):
    query = f"SELECT id from {category_table} WHERE name=\"{category_val}\";"
    print(query)
    return sql_exec_ret_first_elem(query)


def insert_to_movies_category(elem_category, category, last_movie_id, last_category_id):
    query = f"INSERT INTO movies_{category} (movie_id, {elem_category}_id) VALUES ({last_movie_id}, {last_category_id});"
    print(query)
    sql_execute(query)


