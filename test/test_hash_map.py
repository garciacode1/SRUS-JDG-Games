import unittest

from app.player_hash_map import PlayerHashMap


class TestHashMap(unittest.TestCase):
    def test_if_put_updates_an_already_existing_player(self):

        player_hash_map = PlayerHashMap()

        player_hash_map.put("p1", "John")
        player_hash_map.put("p1", "Peter")

        player = player_hash_map.get("p1")

        self.assertEqual("Peter", player.name)
        self.assertEqual(1, player_hash_map.size())

    def test_get_nonexistent_player(self):

        player_hash_map = PlayerHashMap()

        player = player_hash_map.get("p20")
        self.assertIsNone(player)


if __name__ == "__main__":
    unittest.main()
