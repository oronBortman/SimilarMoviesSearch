from utils.general_db_functions import *

similar_movies_cache = {}


def check_similar_movies_in_cache(movie_id):
    return similar_movies_cache.get(movie_id) is not None


def add_similar_movies_to_cache(movie_id, similar_movies_json):
    similar_movies_cache[movie_id] = similar_movies_json


def get_similar_movies_by_category(name_single, name_plural, weight):
    category_id = f'{name_single}_id'
    movies_category = f'movies_{name_plural}'

    return f"""SELECT S.{MOVIE_ID}, ( C.sum2 / GREATEST(
    count(*),
    (SELECT count(*) FROM {movies_category} WHERE {MOVIE_ID} = @movie_id))) *  {weight}  as sum
    FROM {movies_category} S
		INNER JOIN (
		SELECT {MOVIE_ID}, count(*) as sum2
		FROM {movies_category}
		WHERE {category_id} IN (
			SELECT {category_id}
			FROM {movies_category}
			WHERE {MOVIE_ID} = @movie_id) AND {MOVIE_ID} != @{MOVIE_ID}
		GROUP BY {MOVIE_ID}
	) C ON S.{MOVIE_ID} = C.{MOVIE_ID} GROUP BY S.{MOVIE_ID}
    """


def get_similar_movies_by_movie_details(property, weight):

    return f"""SELECT id as movie_id, {weight} as sum
			FROM movies
			WHERE {property} = (SELECT {property} FROM movies WHERE id = @movie_id) AND id != @movie_id
    """


def build_query_similar_movies(movie_id):
    query = f"SET @{MOVIE_ID} = {movie_id};\n"
    query += 'SELECT'
    for property in MOVIE_DETAILS_WITH_ID:
        query += f" {property}"
        if property != MOVIE_DETAILS_WITH_ID[-1]:
            query += ','
    query += f""" FROM movies 
    INNER JOIN (
        SELECT {MOVIE_ID}, SUM(sum) AS 'Total'
        FROM("""
    for category in MOVIE_CATEGORIES:
        name_single = category[0]
        name_plural = category[1]
        weight = category[2]
        query += get_similar_movies_by_category(name_single, name_plural, weight)
        if category != MOVIE_CATEGORIES[-1]:
            query += "Union All\n"
    for property in MOVIE_DETAILS_WEIGHTS:
        name = property[0]
        weight = property[1]
        if category != MOVIE_DETAILS_WEIGHTS[-1]:
            query += "Union All\n"
        query += get_similar_movies_by_movie_details(name, weight)
    query += f"""
    )categories GROUP BY {MOVIE_ID} ORDER BY Total DESC LIMIT {NUMBER_OF_SIMILAR_MOVIES}) as top_similar_movies
    ON top_similar_movies.{MOVIE_ID}=movies.id;
    """
    return query


def gen_movies_details_json(similar_movies):
    similar_movies_json = '['
    for movie in similar_movies:
        similar_movies_json += '{'
        similar_movies_json += generate_movie_details_json(movie)
        similar_movies_json += '}'
        if movie != similar_movies[-1]:
            similar_movies_json += ','
    similar_movies_json += ']'
    return similar_movies_json


def generate_movie_details_json(movie):
    movie_json = ""
    j = 0
    #
    for property in MOVIE_DETAILS_WITH_ID:
        movie_json += f'"{property}":'
        movie_json += '"' + str(movie[j]).replace('"', '\\"') + '"'
        if property != MOVIE_DETAILS_WITH_ID[-1]:
            movie_json += ','
        j += 1
    return movie_json


def get_movies_from_db(query):
    try:
        globals_variables.db = create_db_connection(HOSTNAME, DB_USER, DB_PASSWD)
        globals_variables.cursor = globals_variables.db.cursor(buffered=True)
        movies = sql_execute_ret(query)
        if not movies:
            return []
        movies_json = gen_movies_details_json(movies)
        return movies_json
    except Exception as error:
        print(error)
    finally:
        globals_variables.cursor.close()
        globals_variables.db.close()


def get_similar_movies(movie_id):
    if check_similar_movies_in_cache(movie_id):
        print("Found movie in cache")
        return similar_movies_cache[movie_id]
    else:
        print("Didn't found movie in cache")
        query = build_query_similar_movies(movie_id)
        similar_movies_json = get_movies_from_db(query)
        add_similar_movies_to_cache(movie_id, similar_movies_json)
        return similar_movies_json


def build_query_movies(starts_with):
    query = 'SELECT'
    for property in MOVIE_DETAILS_WITH_ID:
        query += f" {property}"
        if property != MOVIE_DETAILS_WITH_ID[-1]:
            query += ','
    query += f" FROM movies WHERE title like '{starts_with}%'"
    return query


def get_movies(starts_with):
    query = build_query_movies(starts_with)
    return get_movies_from_db(query)
