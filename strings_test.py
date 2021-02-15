import unittest
from unittest import TestCase

from strings import player
from strings import computer
from strings import game

class TestPlayer(TestCase):
    def test_player_returns_valid_char(self):
        assert player() in ['R', 'P', 'S', 'L', 'V']
        print(("Test Passed"))


class TestComputer(TestCase):
    def test_player_returns_valid_char(self):
        self.assertIn(computer(), ['R', 'P', 'S', 'L', 'V'])
        print(("Test Passed"))


class TestGame(TestCase):
    def test_game_returns_bool(self):
        self.assertTrue(type(game(player(),computer())) == bool)
        print(("Test Passed"))




if __name__ == '__main__':
    unittest.main()
