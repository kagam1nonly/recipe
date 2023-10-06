import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import AllRecipe from './pages/AllRecipe';
import AddRecipe from './pages/AddRecipe';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/all-recipes" element={<AllRecipe />} />
          <Route path="/add-recipe" element={<AddRecipe />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
