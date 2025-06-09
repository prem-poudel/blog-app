export async function fetchPosts() {
  const API_URL = 'http://127.0.0.1:8000/api/blog/public/';
  try {
    const response = await fetch(API_URL, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
    return data;
    
  } catch (error) {
    console.error('Error fetching posts:', error);
    return [];
  }
}
