import unittest
from app.player import Player
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def test_insert_head_when_list_is_empty(self):
        player = Player("p1", "John")

        player_list = PlayerList()

        player_list.insert_head(player)

        self.assertEqual(player, player_list.head.player)
        self.assertEqual(player, player_list.tail.player)

    def test_insert_head_when_list_is_not_empty(self):
        first_player = Player("p1", "John")
        second_player = Player("p2", "Lauren")

        player_list = PlayerList()

        player_list.insert_head(first_player)
        player_list.insert_head(second_player)

        self.assertEqual(second_player, player_list.head.player)
        self.assertEqual(first_player, player_list.head.next.player)
        self.assertEqual(player_list.head, player_list.head.next.previous)
        self.assertEqual(first_player, player_list.tail.player)

    def test_insert_tail_when_list_is_not_empty(self):

        first_player = Player("p1", "John")
        second_player = Player("p2", "Lauren")

        player_list = PlayerList()

        player_list.insert_tail(first_player)
        player_list.insert_tail(second_player)

        self.assertEqual(first_player, player_list.head.player)
        self.assertEqual(second_player, player_list.tail.player)
        self.assertEqual(second_player, player_list.head.next.player)
        self.assertEqual(first_player, player_list.tail.previous.player)

    def test_delete_item_from_head(self):

        first_player = Player("p1", "John")
        second_player = Player("p2", "Lauren")
        player_list = PlayerList()

        player_list.insert_tail(first_player)
        player_list.insert_tail(second_player)

        player_list.delete_item_from_head()

        self.assertEqual(second_player, player_list.head.player)
        self.assertIsNone(player_list.head.previous)

    def test_delete_item_from_tail(self):
        first_player = Player("p1", "John")
        second_player = Player("p2", "Lauren")
        player_list = PlayerList()

        player_list.insert_tail(first_player)
        player_list.insert_tail(second_player)

        player_list.delete_item_from_tail()

        self.assertEqual(first_player, player_list.tail.player)
        self.assertIsNone(player_list.tail.next)

    def test_delete_item_by_key(self):

        first_player = Player("p1", "John")
        second_player = Player("p2", "Lauren")

        player_list = PlayerList()

        player_list.insert_tail(first_player)
        player_list.insert_tail(second_player)

        player_list.delete_item_by_key("p1")

        self.assertEqual(second_player, player_list.head.player)


if __name__ == '__main__':
    unittest.main()
