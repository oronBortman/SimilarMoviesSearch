import React, {Component} from "react";
import SearchBar from './SearchBar.js';
import SimilarMoviesList from './SimilarMoviesList'
import MoviesList from "./MoviesList.js";
import './App.css';

class App extends Component {
  state = {
    similar_movies: null,
    movies: null
  };

  fetchMovies = (startsWith) => {
    if(startsWith == '')
    {
      this.setState({
        movies: null,
        similar_movies: null
      })
    }
    else
    {
      const url =`http://127.0.0.1:5000/movies?startsWith=${startsWith}`
      fetch(url)
        .then((result) => result.json())
        .then((result) => {
          console.log("result")
          console.log(result)
          if (result.length == 0)
          {
            this.setState({ movies: null, similar_movies: null});
          }
          else
          {
            this.setState({ movies: result, });
          }
        })
    }
  }

  fetchSimilarMovies = (movie_id) => {
    if(movie_id == '' || movie_id == null)
    {
      this.setState({
        similar_movies: null,
      })
    }
    console.log("movie id:")
    console.log(movie_id)
    const url =`http://127.0.0.1:5000/similar_movies?id=${movie_id}`

    fetch(url)
      .then((result) => result.json())
      .then((result) => {
        this.setState({
          similar_movies: result,
        })
      })
  }

  render() {
    const { similar_movies, movies } = this.state;
    console.log("movies:")
    console.log(movies)
    console.log(similar_movies)

    return (
      <div>
          <div className="container">
              <h1 className = "headline">Find similar movies</h1>
              <SearchBar fetchMovies = {this.fetchMovies} />
              <MoviesList movies = {movies} fetchSimilarMovies = {this.fetchSimilarMovies}/>
              <SimilarMoviesList
                similar_movies = {similar_movies}
              />
          </div>
      </div>
    )
  }
}
/*
*/
export default App;
