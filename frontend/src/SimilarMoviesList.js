import React, {Component} from 'react';

class SimilarMoviesList extends Component {
    constructor(props) {
        super(props);
        this.result = null;
    }

    render(){
        if(this.props.similar_movies != [] && this.props.similar_movies != null)
        {
            this.result = this.props.similar_movies.map((movie) => {
                if(movie.release_date == "None")
                {
                    movie.release_date = "";
                }
                return (
                    <li>{movie.title} {movie.release_date}</li>
                );
            });
            return <div className="similar-movies"><h2>Similar movies</h2><list>{this.result}</list></div>; 
        } 
        else
        {
            return null;
        }          
    }

}

export default SimilarMoviesList;