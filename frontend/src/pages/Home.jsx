// pages/Home.jsx
import React, { useEffect, useState } from 'react';
import { fetchPosts } from '../utils/api';

const Home = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await fetchPosts();
        setPosts(data.data || []);
      } catch (err) {
        setError('Failed to load posts.');
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  return (
    <main className="max-w-4xl mx-auto mt-6 p-4">
      <h2 className="text-2xl font-semibold mb-4">Latest Posts</h2>

      {loading && <p className="text-gray-600">Loading posts...</p>}
      {error && <p className="text-red-600">{error}</p>}

      {!loading && posts.length === 0 && !error && (
        <p className="text-gray-600">No posts available.</p>
      )}

      {posts.map((post) => (
        <article key={post?.uid} className="mb-6 p-4 border rounded shadow-sm">
          <h3 className="text-xl font-bold mb-2">{post?.title}</h3>
          <p className="text-gray-700">{post?.excerpt}</p>
        </article>
      ))}
    </main>
  );
};

export default Home;
