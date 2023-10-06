import React, { useState, useEffect } from 'react';
import './Recipes.css';

function AllRecipe() {
  // State to store the list of recipes fetched from the API
  const [recipes, setRecipes] = useState([]);

  // Function to fetch data from the API
  const fetchRecipes = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/recipe_app/');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setRecipes(data); // Update the state with the fetched data
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  // Fetch data from the API when the component mounts
  useEffect(() => {
    fetchRecipes();
  }, []);

  return (
    <div className="AllRecipe">
      <h1 id="h1">All Recipe</h1>
      <a href="/" className="back-button">
        Back to Home page
      </a>
      <div className='container'>
        {recipes.map((recipe, index) => (
          <div className="product-card" key={index}>
            <h2 style={{textAlign: 'center'}}>{recipe.name}</h2>
            <p className='ingredients'>Ingredients: {recipe.ingredient}</p>
            <p className='procedures'>Procedures: {recipe.procedures}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AllRecipe;
