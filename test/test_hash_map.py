import unittest

from app.player_hash_map import PlayerHashMap


class TestHashMap(unittest.TestCase):

    def test_get_nonexistent_player(self):
        player_hash_map = PlayerHashMap()

        player = player_hash_map.get("p20")
        self.assertIsNone(player)


if __name__ == "__main__":
    unittest.main()
