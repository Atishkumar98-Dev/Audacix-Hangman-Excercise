# Hangman Game API (Django REST + React)

This is a full-stack web application that powers a Hangman game using a Django Rest Framework (DRF) API for the backend and a React.js application for the frontend. The backend manages the game logic, including the selection of words, tracking guesses, and maintaining the state of the game. The frontend interacts with this API and provides a simple UI for players to play the game.

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Prerequisites](#prerequisites)
4. [Backend Setup (Django)](#backend-setup-django)
5. [Frontend Setup (React)](#frontend-setup-react)
6. [API Endpoints](#api-endpoints)
7. [Game Logic](#game-logic)
8. [License](#license)

---

## Features

- Start a new game and get a random word to guess.
- Make guesses, with a limit on the number of incorrect guesses.
- The backend tracks game state, including won, lost, and in-progress status.
- The frontend displays the current game state and allows the user to make guesses.

## Technologies Used

- **Backend**: Python, Django, Django Rest Framework
- **Frontend**: React.js
- **Database**: SQLite (default for Django)

---

## Prerequisites

- Python 3.9+
- Node.js 14+ (for the frontend)
- Git (to clone the repository)

---

## Backend Setup (Django)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/hangman-game.git
cd hangman-game/config
```

### 2. Create a virtual environment

It's recommended to create a virtual environment for Python dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

Make sure you have the necessary Python packages installed. Create a `requirements.txt` file in the backend directory (if it doesn't already exist) with the following content:

```plaintext
Django==4.2
djangorestframework==3.14.0
```

Then install them:

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Since we're using SQLite (the default), you don't need any additional setup for the database. Just run the migrations:

```bash
python manage.py migrate
```

### 5. Create a Django superuser (optional)

If you want to access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

### 6. Run the server

You can start the Django development server with:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

--- 

## Frontend Setup (React)

### 1. Navigate to the frontend directory

```bash
cd ../hangman-frontend
```

### 2. Install frontend dependencies

Make sure you have the necessary Node.js packages installed. Create a `package.json` file in the frontend directory (if it doesn't already exist) with the following content:

```json
{
  "name": "hangman-frontend",
  "version": "1.0.0",
  "dependencies": {
    "axios": "^0.27.2",
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-scripts": "5.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

Then install them:

```bash
npm install
```

### 3. Start the React app

You can start the React development server with:

```bash
npm start
```

The frontend will be accessible at `http://localhost:3000/`.

---

## API Endpoints

Here are the primary API endpoints for the Hangman game:

- **POST /game/start/**: Start a new game and get a random word to guess.
- **POST /game/guess/**: Make a guess and receive feedback on the current game state.

---

## Game Logic

- The game selects a random word from a predefined list.
- Players can make guesses until they either win or exceed the maximum number of incorrect guesses.
- The current game state (in-progress, won, or lost) is maintained on the backend and communicated to the frontend.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to modify any sections as needed!
