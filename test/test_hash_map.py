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

    def test_get_existent_player(self):
        player_hash_map = PlayerHashMap()

        player_hash_map.put("p1", "John")
        player_hash_map.put("p2", "Peter")

        player = player_hash_map.get("p2")

        self.assertEqual("Peter", player.name)
        self.assertEqual("p2", player.uid)

    def test_get_nonexistent_player(self):
        player_hash_map = PlayerHashMap()

        player = player_hash_map.get("p20")
        self.assertIsNone(player)

    def test_remove_existing_player(self):
        player_hash_map = PlayerHashMap()

        player_hash_map.put("p1", "John")
        player_hash_map.remove("p1")

        self.assertEqual(0, player_hash_map.size())

    def test_remove_nonexistent_player(self):
        player_hash_map = PlayerHashMap()

        player_hash_map.put("p1", "John")
        player_hash_map.put("p2", "Daniel")
        player_to_be_removed = player_hash_map.remove("p4")

        self.assertIsNone(player_to_be_removed)
        self.assertEqual(2, player_hash_map.size())

    def test_if_size_increases_properly(self):

        player_hash_map = PlayerHashMap()

        player_hash_map.put("p1", "John")
        player_hash_map.put("p2", "Daniel")
        player_hash_map.put("p3", "Monique")
        player_hash_map.put("p4", "Nelson")

        self.assertEqual(4, player_hash_map.size())

    def test_if_size_decreases_properly(self):
        player_hash_map = PlayerHashMap()

        player_hash_map.put("p1", "John")
        player_hash_map.put("p2", "Daniel")
        player_hash_map.put("p3", "Monique")
        player_hash_map.put("p4", "Nelson")

        player_hash_map.remove("p4")
        player_hash_map.remove("p3")
        player_hash_map.remove("p2")

        self.assertEqual(1,player_hash_map.size())

    def test_collision_players_are_retrieves_accurately(self):
        player_hash_map = PlayerHashMap()

        player_hash_map.put("p1", "John")
        player_hash_map.put("p21", "Daniel")
        player_hash_map.put("p31", "Monique")

        first_player_added = player_hash_map.get("p1")
        second_player_added = player_hash_map.get("p21")
        third_player_added = player_hash_map.get("p31")

        self.assertEqual("John", first_player_added.name)
        self.assertEqual("Daniel", second_player_added.name)
        self.assertEqual("Monique", third_player_added.name)
        self.assertEqual(3, player_hash_map.size())



if __name__ == "__main__":
    unittest.main()
