from app.player_node import PlayerNode


class PlayerList:
    """Double linked list for storing players"""

    def __init__(self):
        self.__head = None

    @property
    def head(self):
        """Return head node at head of list"""
        return self.__head

    @property
    def is_empty(self):
        """Return true if list is empty"""
        return self.__head is None

    def insert_head(self, player):
        new_node = PlayerNode(player)

        if self.__head is None:
            self.__head = new_node
        else:
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__head = new_node
