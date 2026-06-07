import unittest
from app.player import Player


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


if __name__ == '__main__':
    unittest.main()
