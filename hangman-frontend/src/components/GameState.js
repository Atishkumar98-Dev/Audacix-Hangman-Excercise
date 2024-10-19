import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './GameState.css';  // Add custom styles

function GameState({ gameId }) {
  const [gameState, setGameState] = useState({});
  const [guess, setGuess] = useState('');

  useEffect(() => {
    if (gameId) {
      
      fetchGameState();
    }
  }, [gameId]);

  const fetchGameState = () => {
    axios.get(`http://localhost:8000/game/${gameId}/`)
      .then(response => {
        setGameState(response.data);
      })
      .catch(error => {
        console.error('Error fetching game state:', error);
      });
  };

  const handleGuess = () => {
    axios.post(`http://localhost:8000/game/${gameId}/guess/`, { guess })
      .then(response => {
        setGameState(response.data);
        setGuess('');  // Clear the guess input
      })
      .catch(error => {
        console.error('Error making a guess:', error);
      });
  };

  return (
    <div className="game-state-container">
      {gameState.status && (
        <>
          <h3>Game Status: {gameState.status}</h3>

          {/* Word display with one character per box */}
          <div className="word-display">
            {gameState.current_state && gameState.current_state.split('').map((char, index) => (
              <span key={index} className="word-box">{char}</span>
            ))}
          </div>

          <p>Incorrect Guesses: {gameState.incorrect_guesses}</p>
          <p>Remaining Guesses: {gameState.max_incorrect_guesses - gameState.incorrect_guesses}</p>

          {gameState.status === 'InProgress' && (
            <>
              <input
                className="input-board"
                type="text"
                maxLength="1"
                value={guess}
                onChange={(e) => setGuess(e.target.value.toUpperCase())}
                placeholder="Enter a letter"
              />
              <button className="button-hangman" onClick={handleGuess}>Make Guess</button>
            </>
          )}
      
          {gameState.status === 'Lost' && (
            <div className="correct-word">
              <h3>Game Over! The correct word was: <strong>{gameState.word}</strong></h3>
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default GameState;
