DB_NAME = "movies_collection"
HOSTNAME = "localhost"
DB_USER = "root"
DB_PASSWD = "Aa123456"

NUMBER_OF_SIMILAR_MOVIES = 3
MOVIE_ID = "movie_id"
MOVIE_CATEGORIES = [("genre", "genres", "0.25"), ("country", "countries", "0.05"), ("language", "languages", "0.2")]
MOVIE_DETAILS = [("title"), ("release_date"), ("movie_box_office_revenue"), ("feature_length")]
MOVIE_DETAILS_WEIGHTS = [("title", "0.35"), ("release_date", "0.05"), ("movie_box_office_revenue", "0.05"), ("feature_length", "0.05")]

MOVIE_DETAILS_WITH_ID = ["id"] + MOVIE_DETAILS
MOVIES_TABLE = "movies_collection"
