import React, {Component} from 'react';
import './App.css'

class MoviesList extends Component {
    constructor(props) {
        super(props);
        this.result = null;
    }

    handleClick = event => {
        const { name, value } = event.target;

        this.setState({
            [name] : value
        });
        this.props.fetchSimilarMovies(value);
      }

    render() { 
        if(this.props.movies != [] && this.props.movies != null)
        {
            console.log(this.props);
            var release_date="";
            this.result = this.props.movies.map((movie) => {
                if(movie.release_date == "None")
                {
                    release_date = "";
                }
                else
                {
                    release_date = movie.release_date;
                }
                return (
                    <li 
                    name="name"
                    value={movie.id}
                    onClick={this.handleClick}
                    >
                    {movie.title} {release_date}
                    </li>
                );
            });
            return <div>
            <h2 className="list-movies-headline">List of movies:</h2>
            <div className="center-col">
                <span>
                <list>
                    <ul>
                    {this.result}
                    </ul>
                </list>
                </span>
            </div>
        </div>; 
        }
        else
        {
            return null;
        }

    }  
}

export default MoviesList;