import unittest

from app.player import Player
from app.player_bst import PlayerBST


class PlayerBSTTest(unittest.TestCase):

    def test_first_inserted_player_becomes_root(self):
        player_bst = PlayerBST()
        player = Player("p1", "John")

        player_bst.insert(player)

        self.assertEqual(player, player_bst.root.player)

    def test_insert_player_to_left_side(self):
        player_bst = PlayerBST()

        root_player = Player("p1", "Marcos")
        left_player = Player("p2", "Eve")

        player_bst.insert(root_player)
        player_bst.insert(left_player)

        self.assertEqual(left_player, player_bst.root.left.player)

    def test_insert_player_to_right_side(self):
        player_bst = PlayerBST()

        root_player = Player("p1", "John")
        right_player = Player("p2", "Marcos")

        player_bst.insert(root_player)
        player_bst.insert(right_player)

        self.assertEqual(right_player, player_bst.root.right.player)

    def test_insert_same_name_does_not_replace_root(self):
        player_bst = PlayerBST()

        player_bst.insert(Player("p1", "John"))
        player_bst.insert(Player("p2", "John"))

        self.assertEqual("p1", player_bst.root.player.uid)
        self.assertEqual("John", player_bst.root.player.name)

    def test_search_returns_none_when_player_is_not_found(self):
        player_bst = PlayerBST()

        player_bst.insert(Player("p1", "John"))
        player_bst.insert(Player("p2", "Eve"))
        player_bst.insert(Player("p3", "Marcos"))

        found_player = player_bst.search("Paul")

        self.assertIsNone(found_player)

    def test_search_finds_player_on_left_side(self):
        player_bst = PlayerBST()

        root_player = Player("p1", "Marcos")
        left_player = Player("p2", "Eve")

        player_bst.insert(root_player)
        player_bst.insert(left_player)

        found_player = player_bst.search("Eve")

        self.assertEqual(left_player, found_player)

    def test_balance_creates_left_and_right_children(self):
        player_bst = PlayerBST()

        player_bst.insert(Player("p1", "Alexis"))
        player_bst.insert(Player("p2", "Bob"))
        player_bst.insert(Player("p3", "Charlie"))

        player_bst.balance()

        self.assertEqual("Alexis", player_bst.root.left.player.name)
        self.assertEqual("Charlie", player_bst.root.right.player.name)


    def test_search_finds_player_on_right_side(self):
        player_bst = PlayerBST()

        root_player = Player("p1", "John")
        right_player = Player("p2", "Marcos")

        player_bst.insert(root_player)
        player_bst.insert(right_player)

        found_player = player_bst.search("Marcos")

        self.assertEqual(right_player, found_player)

    def test_balance_keeps_all_players_searchable(self):
        player_bst = PlayerBST()

        player_bst.insert(Player("p1", "Alexis"))
        player_bst.insert(Player("p2", "Benny"))
        player_bst.insert(Player("p3", "Celine"))
        player_bst.insert(Player("p4", "David"))
        player_bst.insert(Player("p5", "Eve"))

        player_bst.balance()

        self.assertEqual("Alexis", player_bst.search("Alexis").name)
        self.assertEqual("Benny", player_bst.search("Benny").name)
        self.assertEqual("Celine", player_bst.search("Celine").name)
        self.assertEqual("David", player_bst.search("David").name)
        self.assertEqual("Eve", player_bst.search("Eve").name)


if __name__ == "__main__":
    unittest.main()
