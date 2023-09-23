"""
Test Module for Game Class
==========================

This module contains the test cases for the `Game` class from `main.game` module. 
The `Game` class manages the game logic, including initializing game models, playing rounds,
evaluating rounds, and updating models based on user inputs.

"""

import unittest
from unittest.mock import MagicMock
from main.game import Game

class TestGame(unittest.TestCase):
    """
    TestCase class for testing the Game class.

    Methods:
        - test_initialization: Tests the initialization of the Game class and its attributes.
        - test_reset_scores: Tests if the reset_scores method is resetting
        the scores dictionary correctly.
        - test_play: Tests the play method, ensuring it calls other methods correctly
        and returns the expected result.
        - test_get_ai_move: Tests if the get_ai_move method retrieves
        the correct move from the models.
        - test_evaluate_round: Tests the evaluate_round method for different scenarios
        to ensure it returns correct results.
        - test_models_update: Tests if the models_update method is updating
        all models correctly with the user's move.
    """

    def test_initialization(self):
        """
        Test if the Game class is initialized with the correct attributes and their default values.
        """
        game = Game(focus=5)
        self.assertEqual(game.focus, 5)
        self.assertEqual(len(game.models), 5)
        self.assertIsNone(game.current_model)
        self.assertDictEqual(game.scores, {"TIE": 0, "WIN": 0, "LOSE": 0})

    def test_reset_scores(self):
        """
        Test if the reset_scores method is correctly resetting
        the scores dictionary and the current_model attribute.
        """
        game = Game(focus=5)
        game.scores = {"TIE": 1, "WIN": 2, "LOSE": 3}
        game.reset_scores()
        self.assertDictEqual(game.scores, {"TIE": 0, "WIN": 0, "LOSE": 0})
        self.assertIsNone(game.current_model)

    def test_play(self):
        """
        Test the play method by mocking dependent methods to ensure
        that all methods are called correctly, and the result is as expected.
        """
        game = Game(focus=5)
        game.get_ai_move = MagicMock(return_value="rock")
        game.models_update = MagicMock()
        game.evaluate_round = MagicMock(return_value=("It's a tie!", "rock"))

        result = game.play("rock")

        game.get_ai_move.assert_called_once()
        game.models_update.assert_called_once_with("rock")
        game.evaluate_round.assert_called_once_with("rock", "rock")
        self.assertEqual(result, ("It's a tie!", "rock"))

    def test_get_ai_move(self):
        """
        Test if the get_ai_move method is correctly getting
        predictions from the models and returning the AI's move.
        """
        game = Game(focus=5)
        for model in game.models:
            model.get_prediction = MagicMock(return_value="rock")
            model.get_score = MagicMock(return_value=1)

        ai_move = game.get_ai_move()
        self.assertEqual(ai_move, "rock")

    def test_evaluate_round(self):
        """
        Test if the evaluate_round method is correctly evaluating
        different round scenarios and returning the expected results.
        """
        game = Game(focus=5)
        self.assertEqual(game.evaluate_round("rock", "scissors"), ('You win!', 'rock'))
        self.assertEqual(game.evaluate_round("rock", "paper"), ('You lose :(', 'rock'))
        self.assertEqual(game.evaluate_round("rock", "rock"), ("It's a tie!", 'rock'))

    def test_models_update(self):
        """
        Test if the models_update method is correctly updating each model with the user's move.
        """
        game = Game(focus=5)
        for model in game.models:
            model.update = MagicMock()

        game.models_update("rock")

        for model in game.models:
            model.update.assert_called_once_with("rock")
