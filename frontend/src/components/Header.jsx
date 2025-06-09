// components/Header.jsx
import React from 'react';

const Header = () => {
  return (
    <header className="bg-gray-800 text-white p-4 shadow">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <h1 className="text-xl font-bold">BlogApp</h1>
        <nav>
          <a href="/" className="mx-2 hover:underline">Home</a>
          <a href="/about" className="mx-2 hover:underline">About</a>
        </nav>
      </div>
    </header>
  );
};

export default Header;
