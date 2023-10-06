import React from 'react';
import './Layout.css'; // Include common layout styles here

function Layout({ children }) {
  return (
    <div className="layout">
      {children}
    </div>
  );
}

export default Layout;