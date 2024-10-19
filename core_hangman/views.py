from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer
from rest_framework.decorators import api_view


# Start a new game
class NewGameView(APIView):
    def post(self, request):
        game = Game()
        game.start_new_game()
        game.save()  # Save the game instance before serializing
        return Response({"game_id": game.id}, status=status.HTTP_201_CREATED)

# Get the game state
class GameStateView(APIView):
    def get(self, request, game_id):
        try:
            game = Game.objects.get(pk=game_id)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

# Make a guess
class GuessView(APIView):
    def post(self, request, game_id):
        try:
            game = Game.objects.get(pk=game_id)
            guess = request.data.get("guess", "").upper()  # Default to empty string
            if not guess or len(guess) != 1:
                return Response({"error": "Invalid guess"}, status=status.HTTP_400_BAD_REQUEST)

            correct, status = game.make_guess(guess)
            response = {
                "correct": correct,
                "status": status,
                "current_state": game.current_state,
                "incorrect_guesses": game.incorrect_guesses,
                "max_incorrect_guesses": game.max_incorrect_guesses,
            }
            if game.status == "Lost":
                response['word'] = game.word  # Include the correct word in the response
            return Response(response)
        
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def game_state(request, game_id):
    try:
        game = Game.objects.get(id=game_id)
        response_data = {
            'status': game.status,
            "word":game.word,
            'current_state': game.current_state,
            'incorrect_guesses': game.incorrect_guesses,
            'max_incorrect_guesses': game.max_incorrect_guesses,
        }
        
        # If the game is lost, include the correct word
        if game.status == "Lost":
            response_data['word'] = game.word  # Include the correct word in the response

        return Response(response_data)
    except Game.DoesNotExist:
        return Response({'error': 'Game not found'}, status=404)
