from django.db import models
from random import choice


class Game(models.Model):
    word_list = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]
    
    word = models.CharField(max_length=100)  # Word selected for this game
    current_state = models.CharField(max_length=100, default="")  # Current state of guessed letters, e.g., 'P__'
    incorrect_guesses = models.IntegerField(default=0)  # Number of incorrect guesses
    max_incorrect_guesses = models.IntegerField()  # Max allowed guesses
    status = models.CharField(max_length=10, default="InProgress")  # Game status: InProgress, Lost, or Won
    guessed_letters = models.CharField(max_length=100, default="")  # Letters guessed so far
    
    def start_new_game(self):
        # Randomly pick a word from the list and initialize the game
        self.word = choice(self.word_list).upper()
        self.current_state = "_" * len(self.word)
        self.max_incorrect_guesses = len(self.word)
        self.save()
    
    def make_guess(self, guess):
        # Handle a new guess
        guess = guess.upper()
        if guess in self.guessed_letters:
            return False, self.status  # Guess has already been made
        
        self.guessed_letters += guess

        if guess in self.word:
            # Reveal the guessed letter in the word
            self.current_state = "".join(
                [char if char == guess or char in self.guessed_letters else "_" for char in self.word]
            )
            if "_" not in self.current_state:
                self.status = "Won"
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_incorrect_guesses:
                self.status = "Lost"
        
        self.save()
        return guess in self.word, self.status
    
    def get_status(self):
        max_incorrect_guesses = len(self.word) - 1

        if self.incorrect_guesses > max_incorrect_guesses:
            return "Lost"
        elif "_" not in self.current_state():
            return "Won"
        else:
            return "InProgress"

    # def current_state(self):
    #     return ''.join([letter if letter.lower() in self.guessed_letters.lower() else "_" for letter in self.word])
