"""
Test Module for MarkovModel
===========================

This module contains the test cases for the `MarkovModel` class. 
The `MarkovModel` class is used for making predictions based on the history of user moves. 
The test module focuses on initializing, updating, resetting, 
focusing, and ordering the MarkovModel.

"""

import unittest
from main.markov_model import MarkovModel

class TestMarkovModel(unittest.TestCase):
    """
    TestCase class for testing the MarkovModel class.

    Methods:
        - test_init: Tests the initialization of the MarkovModel.
        - test_update_and_score: Tests the update method and the score after each move.
        - test_reset: Tests if the reset method is resetting the model's state.
        - test_focus_limit: Tests if the score_history's length doesn’t exceed the focus.
        - test_order_limit: Tests if the user_moves's length doesn’t exceed the order.
    """

    def test_init(self):
        """
        Test if the MarkovModel class is initialized with the correct attributes
        and their default values.
        """
        model = MarkovModel(order=3, focus=5)
        self.assertEqual(model.order, 3)
        self.assertEqual(model.focus, 5)
        self.assertEqual(model.user_moves, [])
        self.assertEqual(model.score_history, [])
        self.assertIsNone(model.ai_move)

    def test_update_and_score(self):
        """
        Test the update method and validate the score after every move
        to ensure correct score calculation and updating.
        """
        model = MarkovModel(order=3, focus=5)
        model.ai_move = 'rock'
        model.update('paper')
        self.assertEqual(model.get_score(), -1)  # User wins

        model.ai_move = 'scissors'
        model.update('scissors')
        self.assertEqual(model.get_score(), -1)  # Tie is zero

        model.ai_move = 'paper'
        model.update('rock')
        self.assertEqual(model.get_score(), 0)  # AI wins -1+0+1

    def test_reset(self):
        """
        Test if the reset method is correctly resetting 
        the user_moves and score_history of the model.
        """
        model = MarkovModel(order=3, focus=5)
        model.ai_move = 'rock'
        model.update('paper')
        model.update('scissors')
        model.reset()
        self.assertEqual(model.user_moves, [])
        self.assertEqual(model.score_history, [])

    def test_focus_limit(self):
        """
        Test if the length of score_history does not exceed
        the focus limit after multiple updates.
        """
        model = MarkovModel(order=3, focus=2)  # focus of 2
        model.ai_move = 'rock'
        model.update('paper')
        model.update('scissors')
        model.update('rock')
        self.assertEqual(len(model.score_history), 2)

    def test_order_limit(self):
        """
        Test if the length of user_moves does not exceed
        the order limit after multiple updates.
        """
        model = MarkovModel(order=2, focus=5)  # order of 2
        model.update('rock')
        model.update('paper')
        model.update('scissors')
        self.assertEqual(len(model.user_moves), 2)
