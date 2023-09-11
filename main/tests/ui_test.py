import unittest
from unittest.mock import patch
from main.ui import game_instance


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = game_instance

    def test_reset_scores(self):
        self.game.reset_scores()
        expected_scores = {"TIE": 0, "WIN": 0, "LOSE": 0}
        self.assertEqual(self.game.scores, expected_scores)

    @patch("random.choice", return_value="rock")
    def test_play_tie(self, mock_choice):
        result, ai_choice = self.game.play("rock")
        self.assertEqual(result, "It's a tie!")
        self.assertEqual(ai_choice, "rock")
        self.assertEqual(self.game.scores["TIE"], 1)

    @patch("random.choice", return_value="scissor")
    def test_play_win(self, mock_choice):
        result, ai_choice = self.game.play("rock")
        self.assertEqual(result, "You win!")
        self.assertEqual(ai_choice, "scissor")
        self.assertEqual(self.game.scores["WIN"], 1)

    @patch("random.choice", return_value="paper")
    def test_play_lose(self, mock_choice):
        result, ai_choice = self.game.play("rock")
        self.assertEqual(result, "You lose :(")
        self.assertEqual(ai_choice, "paper")
        self.assertEqual(self.game.scores["LOSE"], 1)

