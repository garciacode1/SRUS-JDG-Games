import unittest
from app.player import Player
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def test_insert_head_when_list_is_empty(self):
        player = Player("p1", "Mike")
        player_list = PlayerList()

        player_list.insert_head(player)
        self.assertEqual(player, player_list.head.player)

    def test_insert_head_when_list_is_not_empty(self):
        first_player = Player("p1", "Mike")
        second_player = Player("p2", "Louis")

        player_list = PlayerList()

        player_list.insert_head(first_player)
        player_list.insert_head(second_player)

        self.assertEqual(second_player, player_list.head.player)
        self.assertEqual(first_player, player_list.head.next.player)
        self.assertEqual(player_list.head, player_list.head.next.previous)


if __name__ == '__main__':
    unittest.main()
