# Usage
## 1.  Create db and import json data to db:
1.1 In create_db_import_json/settings/configuration.py 
edit the following properties by your MySQL instace:
```
HOSTNAME 
DB_USER
DB_PASSWD
```

1.2 Open terminal and run the following command:
```
pip install mysql-connector-python
cd create_db_import_json
python main.py
```
      
## 2. Start the backend api server:
open terminal and run the following command:
```
pip install Flask
cd backend
flask run
```
## 4. Start the web application:
open terminal and run the following command:
```
cd forntend
npm install
npm run
```

#Techincal Infomration

## 1. DB design - MySQL

Relationships in the DB:

The categories: countries, genres and languages have many-to-many relationships with the movies.

therefore I used the movies_category (e.g: movies_genres, movies_countries) tables to split the many-to-many relationship to one-to-many and many-to-one relationships as follows:

● one-to-many - from the movies table to movies_category table

● many-to-one - from movies_category table to category table

Keys in the DB:

I used the id column as the primary key in the movies, countries, genres and languages tables, because it is always unique.

I defined movie_id and category_id as foreign keys in the movies_category table, because they refer to the movies and categories tables.

Also, I defined the primary key in the movies_category to be (movie_id, genre_id) because movie_id in every row 
is not unique and genre_id in every row is not unique, but they are both unique in every row.
    
## 2. The similar movies algorithm

I gave a weight percent for every feature of the movies as follows:

title - 0.35, genres - 0.25, countries - 0.05, languages - 0.2,
release_date - 0.05, movie_box_office_revenue - 0.05, feature_length - 0.05

I defined the weights of the categories by how I think similar movies are suppose to be defined.

The algorithm:

1. Get the categories values of the selected movie: languages, countries and genres 2. For every category:

      2.1 Get all the rows from movies_category table by the category values ids of the selected movie except of the rows that the movie_id of the selected movie appears in them

      2.2 Sum the number of appearances of every movie in the rows

      2.3 Calculate the maximum between the number of the category values of every movie and the number of category values of the selected movie

      2.4 Divide the result of section 2.2 by the result of section 2.3 for every movie

      2.5 Multiply the result by the weight of the category for every movie

      2.6 Add the result of every movie to its sum of weights

3. Get the top three movies that their sum of weights is the biggest

## 3. Create db and import to json

Usage of Template design pattern:
The create db and import from json to db algorithms have the same skelethon of connecting to the db and then doing actions on the db, 
committing them and closing the connection. Therefore, to avoid code duplication, I used a template class and I called it ActionsOnDB. This class has the function “operation_on_db” as an injection point to run actions on the db. The classes CreateDB and ImportJsonToDb inherit from the ActionsOnDB class and the “operation_on_db” is configured with the actions that each algorithm does in the db.

Algorithm for importing the json data to the db:
remark: The algorithm reads every line of the json file and not all the json file as a whole json object, because the given json file has a root element in every line and as far as I know it’s not a valid json format and json should have one root element.

1. For every line in the json file:

      a. create json object
      
      b. insert data to the db tables based on the json object
      
## 4. Backend - flask
API methods:

      ● /movies?startsWith=value:
            returns all the movies that starts with the given value
      ● /similar_movies?id=value:
            returns the top three movies that are similar to the movie with the given id
            
There is a local cache (dictionary of python) that holds the similar movies that were fetched from the server.

## 5. Frontend - React
