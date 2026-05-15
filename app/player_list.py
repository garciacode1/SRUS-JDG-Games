from app.player_node import PlayerNode


class PlayerList:
    """Double linked list for storing players"""

    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        """Return head node at head of list"""
        return self.__head

    @property
    def tail(self):
        """Return tail node at tail of list"""
        return self.__tail

    @property
    def is_empty(self):
        """Return true if list is empty"""
        return self.__head is None

    def insert_head(self, player):
        """Insert player at head of list"""
        new_node = PlayerNode(player)

        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node

        else:
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__head = new_node

    def insert_tail(self, player):
        """Function to insert player at tail of list"""

        new_node = PlayerNode(player)

        if self.is_empty:
            self.__tail = new_node
            self.__head = new_node
        else:
            new_node.previous = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node
