import unittest
from src.game import game_instance

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game_instance

    def test_game_initial_values(self):
        self.assertEqual(self.game.scores["WIN"], 0)
        self.assertEqual(self.game.scores["LOSE"], 0)
        self.assertEqual(self.game.scores["TIE"], 0)
    def test_game_initial_values(self):
        self.assertEqual(self.game.scores["WIN"], 0)
        self.assertEqual(self.game.scores["LOSE"], 0)
        self.assertEqual(self.game.scores["TIE"], 0)