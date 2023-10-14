"""
    Tests for the MarkovModel class.
"""

import unittest
from main.markov_model import MarkovModel

class TestMarkovModel(unittest.TestCase):
    """
    Test suite for the MarkovModel class.
    """

    def setUp(self):
        """
        Set up a new instance of the MarkovModel class before each test.
        """
        self.model = MarkovModel(order=3, focus=5)

    def test_initialization(self):
        """
        Test to ensure that the MarkovModel is correctly initialized.
        """
        self.assertEqual(self.model.order, 3)
        self.assertEqual(self.model.focus, 5)
        self.assertEqual(len(self.model.user_moves), 0)
        self.assertEqual(len(self.model.score_history), 0)

    def test_update(self):
        """
        Test the update method to ensure the model gets updated correctly.
        """
        self.model.update('rock')
        self.assertEqual(len(self.model.user_moves), 1)
        self.assertIn('rock', self.model.user_moves)

    def test_get_prediction(self):
        """
        Test the get_prediction method to ensure predictions are being made.
        """
        predictions = {self.model.get_prediction() for _ in range(20)}
        self.assertEqual(predictions, {'rock', 'paper', 'scissors'})

    def test_evaluate_move(self):
        """
        Test the evaluate_move method to ensure moves are evaluated correctly.
        """
        self.model.ai_move = 'rock'
        self.assertEqual(self.model.evaluate_move('scissors'), 1)  # AI wins
        self.assertEqual(self.model.evaluate_move('rock'), 0)      # Tie
        self.assertEqual(self.model.evaluate_move('paper'), -1)    # User wins

    def test_get_score(self):
        """
        Test the get_score method to ensure that the score is correctly calculated.
        """
        self.model.score_history = [1, 0, -1, 1, 1]
        self.assertEqual(self.model.get_score(), 2)

    def test_reset(self):
        """
        Test the reset method to ensure the model is correctly reset.
        """
        self.model.update('rock')
        self.model.update('paper')
        self.model.reset()

        self.assertEqual(len(self.model.user_moves), 0)
        self.assertEqual(len(self.model.score_history), 0)

    def test_pattern_prediction(self):
        """
        Test model making actual predictions
        """
        # Feed the model a repeating pattern and see if it can predict and counter it.
        pattern = ['rock', 'rock', 'rock']

        for move in pattern:
            self.model.update(move)

        # After seeing the pattern, the model should predict 'rock' next,
        # and therefore, it should counter with 'paper'.
        prediction = self.model.get_prediction()
        self.assertEqual(prediction, 'paper')
