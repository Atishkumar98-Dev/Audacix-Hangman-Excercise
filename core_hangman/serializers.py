from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'word', 'current_state', 'incorrect_guesses', 'max_incorrect_guesses', 'status', 'guessed_letters']
        read_only_fields = ['word', 'current_state', 'status', 'incorrect_guesses', 'max_incorrect_guesses', 'guessed_letters']
