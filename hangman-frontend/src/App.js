import React, { useEffect, useState } from 'react';
import './App.css';
import NewGame from './components/NewGame';
import GameState from './components/GameState';

function App() {
  const [gameId, setGameId] = useState(null);

  useEffect(() => {
    // Check if there's a game ID in local storage when the component mounts
    const storedGameId = localStorage.getItem('gameId');
    if (storedGameId) {
      setGameId(Number(storedGameId));  // Convert stored ID to a number
    }
  }, []);

  const handleSetGameId = (id) => {
    setGameId(id);
    // Save the game ID to local storage
    localStorage.setItem('gameId', id);
  };

  return (
    <div>
      {!gameId ? (
        <NewGame setGameId={handleSetGameId} />
      ) : (
        <GameState gameId={gameId} setGameId={handleSetGameId} />  // Pass setGameId to GameState
      )}
    </div>
  );
}

export default App;
