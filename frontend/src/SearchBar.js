import React, {Component} from 'react';

class SearchBar extends Component {
    constructor(props) {
        super(props);
        this.initialState = {
            name: ''
        };
        this.state = this.initialState;
    }

    handleChange = event => {
        const { name, value } = event.target;

        this.setState({
            [name] : value
        });
        this.props.fetchMovies(value);
    }

    render() {
        const { name } = this.state;
    
        return (
        <form className="search-bar">
            <label htmlFor="name">Search Movies: </label>
            <input
            type="text"
            name="name"
            value={name}
            onChange={this.handleChange} 
           />
        </form>
        );
    }
}

export default SearchBar;