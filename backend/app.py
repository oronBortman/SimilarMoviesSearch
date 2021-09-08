import json
from flask import request
import flask
from flask import Flask, jsonify, send_file
app = Flask(__name__)
from utils.similar_movies import *


def get_json(data):
    jarray = json.loads(data)
    response = flask.jsonify(jarray)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app = Flask(__name__)


@app.route("/movies", methods=["GET"])
def movies():
    starts_with = request.args.get('startsWith')
    if starts_with == '':
        return "null"
    movies = get_movies(starts_with)
    if movies == []:
        response = get_json(str(movies))
    else:
        response = get_json(movies)
    return response


@app.route("/similar_movies", methods=["GET"])
def similar_movies():
    movie_id = request.args.get('id')
    similar_movies = get_similar_movies(movie_id)
    response = get_json(similar_movies)
    return response


if __name__ == '__main__':
    app.run()
