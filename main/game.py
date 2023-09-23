
"""
    Rock-Paper-Scissors Game with Markov Models
    ===========================================

    This module provides a `Game` class to simulate a rock-paper-scissors game 
    against an AI opponent that leverages multiple Markov Models for predictions. 
    The AI evaluates the performance of these models over a specified number of rounds 
    (determined by the `focus` attribute) to select the best-performing model.

    The game logic and flow are managed by the `Game` class, while the predictive 
    intelligence is encapsulated within the Markov Models.

    Usage:
        game_instance = Game(focus=5)
        game_instance.play("rock")
        # The AI makes a move in response, and the game outcome is recorded.

    Dependencies:
        - MarkovModel class from the `main.markovModel` module.

    Classes:
        - Game
"""

from main.markov_model import MarkovModel

class Game:
    """
    Represents a rock-paper-scissors game leveraging multiple Markov Models 
    to predict and counter user moves and evaluate their performance over a 
    specified number of rounds (focus).

    Attributes:
        focus (int): Number of rounds to evaluate each Markov Model's performance.
        choices (list): Possible move choices in the game.
        scores (dict): Tracks the game outcomes.
        models (list): Collection of Markov Models.
        current_model (int or None): Index of the current model being used.
    """

    def __init__(self, focus):
        """
        Initialize a new instance of the Game class.
        
        :param focus: The number of rounds to evaluate each Markov Model's performance.
        """
        self.focus = focus
        self.choices = ["rock", "paper", "scissors"]
        self.models = [MarkovModel(i, focus) for i in range(1, 6)]
        self.current_model = None  # Initialize current_model attribute here
        self.reset_scores()

    def reset_scores(self):
        """
        Reset game scores and underlying models.
        """
        self.scores = {"TIE": 0, "WIN": 0, "LOSE": 0}
        for model in self.models:
            model.reset()
        self.current_model = None

    def play(self, user_move):
        """
        Play a round of the game using the user's move.
        
        :param user_move: The user's move played in the current round.
        """
        ai_move = self.get_ai_move()
        self.models_update(user_move)
        return self.evaluate_round(ai_move, user_move)

    def get_ai_move(self):
        """
        Get the AI's predicted move for the current round.
        
        :return: The AI's predicted move.
        """
        predictions = [model.get_prediction() for model in self.models]
        self.current_model = self.models.index(
            max(self.models, key=lambda model: model.get_score()))
        return predictions[self.current_model]

    def evaluate_round(self, ai_move, user_move):
        """
        Evaluate the result of the round and update the scores.
        
        :param ai_move: The AI's move played in the current round.
        :param user_move: The user's move played in the current round.
        """
        win_conditions = [('rock', 'paper'), ('paper', 'scissors'), ('scissors', 'rock')]
        lose_conditions = [('paper', 'rock'), ('scissors', 'paper'), ('rock', 'scissors')]

        if (ai_move, user_move) in lose_conditions:
            self.scores['WIN'] += 1
            return 'You win!', ai_move
        elif (ai_move, user_move) in win_conditions:
            self.scores['LOSE'] += 1
            return 'You lose :(', ai_move
        else:
            self.scores['TIE'] += 1
            return "It's a tie!", ai_move

    def models_update(self, user_move):
        """
        Update all Markov Models with the latest user_move.
        
        :param user_move: The user's move played in the current round.
        """
        for model in self.models:
            model.update(user_move)

# Create a Game instance with a focus of 5 rounds
game_instance = Game(5)
