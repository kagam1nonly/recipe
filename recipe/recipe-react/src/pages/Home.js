import React from 'react';
import { Link } from 'react-router-dom'; // Import Link from react-router-dom
import './Home.css';

function Home() {
  return (
    <div className="Home">
      <div className="button-container">
        {/* Use Link component to navigate to "/all-recipes" */}
        <Link to="/all-recipes" className="box1">
          All Recipe
        </Link>
        {/* Use Link component to navigate to "/add-recipe" */}
        <Link to="/add-recipe" className="box2">
          Add Recipe
        </Link>
      </div>
    </div>
  );
}

export default Home;
