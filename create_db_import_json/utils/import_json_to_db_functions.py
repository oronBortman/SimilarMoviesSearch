import json

from utils.insert_to_db_functions import *
from utils.action_on_db import *


class ImportJsonToDB(ActionsOnDB):

    def __iterate_on_category(self, data, elem_category, category, movie_id):
        for i in data[category]:
            category_val = data[category][i].replace('"', '\\"')
            if not check_if_category_exists(category, category_val):
                insert_category_val(category, category_val)
            category_id = get_category_id(category, category_val)
            insert_to_movies_category(elem_category, category, movie_id, category_id)


    def __check_if_key_exists(self, data, keys):
        for key in keys:
            if key not in data:
                return False
        return True

    def __add_details_to_movie(self, data, movie_details):
        movie_values = []
        for movie_detail in movie_details:
            detail_val = "NULL"
            if data[movie_detail] != "":
                detail_val = '"' + data[movie_detail].replace('"', '\\"') + '"'
            movie_values.append(detail_val)
        title, release_date, movie_box_office_revenue, plot_summary, feature_length = movie_values
        movie_id = insert_movie_to_movies_table(title, release_date, movie_box_office_revenue, plot_summary,
                                                feature_length)
        return movie_id

    def __import_json_to_db(self):
        movie_categories = list(map(lambda x: x[1], MOVIE_CATEGORIES))
        keys = MOVIE_DETAILS + movie_categories
        with open(JSON_FILE) as f:
            for line in f:
                data = json.loads(line)
                if not self.__check_if_key_exists(data, keys):
                    continue
                movie_id = self.__add_details_to_movie(data, MOVIE_DETAILS)
                for elem_category, category, _ in MOVIE_CATEGORIES:
                    self.__iterate_on_category(data, elem_category, category, movie_id)

    def operation_on_db(self) -> None:
        self.__import_json_to_db()

