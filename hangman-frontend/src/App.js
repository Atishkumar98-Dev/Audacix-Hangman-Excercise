import React, { useState } from 'react';
import './App.css';
import NewGame from './components/NewGame';
import GameState from './components/GameState';

function App() {
  const [gameId, setGameId] = useState(null);

  return (
    <div className="App">
      <h1>Hangman Game</h1>
      {!gameId ? (
        <NewGame setGameId={setGameId} />
      ) : (
        <GameState gameId={gameId} />
      )}
    </div>
  );
}

export default App;
