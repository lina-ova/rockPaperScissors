"""Unit Tests for Rock Paper Scissors Game.

This module contains a series of tests to validate the functionalities of
the Rock Paper Scissors game. The game instance from the main.game module is
utilized to perform these tests.
"""

import unittest
from unittest.mock import patch
from main.game import game_instance


class TestGame(unittest.TestCase):
    """Unit Test Suite for verifying Rock Paper Scissors game functionality."""

    def setUp(self):
        """Setup method to initialize game instance before each test."""
        self.game = game_instance

    def test_reset_scores(self):
        """Ensure that scores are reset correctly."""
        self.game.scores = {"TIE": 1, "WIN": 2, "LOSE": 3}
        self.game.reset_scores()
        expected_scores = {"TIE": 0, "WIN": 0, "LOSE": 0}
        self.assertEqual(self.game.scores, expected_scores)

    @patch("random.choice", return_value="rock")
    def test_play_tie(self, _):
        """Ensure that a tie scenario works correctly."""
        result, ai_choice = self.game.play("rock")
        self.assertEqual(result, "It's a tie!")
        self.assertEqual(ai_choice, "rock")
        self.assertEqual(self.game.scores["TIE"], 1)

    @patch("random.choice", return_value="scissor")
    def test_play_win(self, _):
        """Ensure that a win scenario works correctly."""
        result, ai_choice = self.game.play("rock")
        self.assertEqual(result, "You win!")
        self.assertEqual(ai_choice, "scissor")
        self.assertEqual(self.game.scores["WIN"], 1)

    @patch("random.choice", return_value="paper")
    def test_play_lose(self, _):
        """Ensure that a lose scenario works correctly."""
        result, ai_choice = self.game.play("rock")
        self.assertEqual(result, "You lose :(")
        self.assertEqual(ai_choice, "paper")
        self.assertEqual(self.game.scores["LOSE"], 1)
