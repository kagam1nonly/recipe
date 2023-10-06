import React, { useState } from 'react';
import './Recipes.css'; 

function AddRecipe() {
  // State to store the form data
  const [formData, setFormData] = useState({
    name: '',
    ingredient: '',
    procedures: '',
  });

  // Function to handle form input changes
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Function to handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Send a POST request to your API endpoint with formData
      const response = await fetch('http://127.0.0.1:8000/api/recipe_app/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      // Clear the form after successful submission
      setFormData({
        name: '',
        ingredient: '',
        procedures: '',
      });

      // Optionally, you can redirect or show a success message here
      alert('Recipe Submitted Successfully!');
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  return (
    <div className='AllRecipe'>
      <h1 id="h1">Add Recipe</h1>
      <a href="/" className="back-button">
        Back to Home page
      </a>
      <div className='container2'>
        <div className="form-box">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="name">Name:</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleInputChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="ingredient">Ingredients:</label>
              <textarea
                id="ingredient"
                name="ingredient"
                value={formData.ingredient}
                onChange={handleInputChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="procedures">Procedures:</label>
              <textarea
                id="procedures"
                name="procedures"
                value={formData.procedures}
                onChange={handleInputChange}
                required
              />
            </div>

            <button type="submit" className="submit-button">
              Submit
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default AddRecipe;