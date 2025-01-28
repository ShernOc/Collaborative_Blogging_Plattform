import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState(null); // State to hold fetched data
  const [error, setError] = useState(null); // State to hold errors
  const apiUrl = 'http://127.0.0.1:5000';

  // Backend Communication with Cors2
  useEffect(() => {
    fetch(`${apiUrl}/`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((json) => setData(json))
      .catch((err) => setError(err.message));
  }, [apiUrl]);

  return (
    <div className="App">
      <h1>Collaborative Blog Platform </h1>
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
