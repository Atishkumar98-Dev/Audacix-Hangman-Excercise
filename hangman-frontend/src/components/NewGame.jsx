// import React, { useState } from 'react';
import axios from 'axios';
import './NewGame.css';  // Import a CSS file for styling

function NewGame({ setGameId }) {
  const startNewGame = () => {
    axios.post('http://localhost:8000/game/new/')
      .then(response => {
        setGameId(response.data.game_id);  // Store game ID in parent component
      })
      .catch(error => {
        console.error('Error starting new game:', error);
      });
  };

  return (
    <div className="new-game-container">
        <img  src={`${process.env.PUBLIC_URL}/images/hangman.jpg`} alt="Hangman" />
      <h1 className="game-title">Hangman Game</h1>
      <div className="hangman-graphic">
      </div>
      <button className="start-game-btn" onClick={startNewGame}>
        Start New Game
      </button>
    </div>
  );
}

export default NewGame;
