import unittest
from app.player import Player


class PlayerTest(unittest.TestCase):

    def test_for_uid_validation(self):
        player = Player("20114823", "Mathew")
        self.assertEqual(player.uid, "20114823")

    def test_for_name_validation(self):
        player = Player("20114823", "Mathew")
        self.assertEqual(player.name, "Mathew")


if __name__ == '__main__':
    unittest.main()
