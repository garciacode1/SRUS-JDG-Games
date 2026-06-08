import unittest
from app.player import Player
import random


class PlayerTest(unittest.TestCase):

    def test_for_uid_validation(self):
        player = Player("20114823", "Mathew")
        self.assertEqual(player.uid, "20114823")

    def test_for_name_validation(self):
        player = Player("20114823", "Mathew")
        self.assertEqual(player.name, "Mathew")

    def test_sort_players(self):
        players = [
            Player("01", "Alice", score=10),
            Player("02", "Bob", score=5),
            Player("03", "Charlie", score=15)
        ]

        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [
            Player("02", "Bob", score=5),
            Player("01", "Alice", score=10),
            Player("03", "Charlie", score=15)
        ]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player("01", "Alice", 10)
        bob = Player("02", "Bob", 5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(bob < alice)

    def test_custom_sort_quickly_sorts_players_by_score_descending(self):
        players = [
            Player("01", "Alice", 10),
            Player("02", "Bob", 5),
            Player("03", "Charlie", 15),
            Player("04", "Paul", 20),
            Player("05", "Matheus", 30),
        ]

        sorted_players = Player.sort_quickly(players)

        manually_sorted_players = [
            Player("05", "Matheus", 30),
            Player("04", "Paul", 20),
            Player("03", "Charlie", 15),
            Player("01", "Alice", 10),
            Player("02", "Bob", 5)

        ]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_custom_sort_quickly_sorts_1000_players(self):
        random.seed(42)

        players = []

        for i in range(1000):
            player = Player(f"{i:03}", f"Player {i}", score=random.randint(0, 1000))
            players.append(player)

        custom_sorted_players = Player.sort_quickly(players)

        custom_scores = []

        for player in custom_sorted_players:
            custom_scores.append(player.score)

        expected_scores = sorted(custom_scores, reverse=True)

        self.assertEqual(expected_scores, custom_scores)

if __name__ == '__main__':
    unittest.main()
