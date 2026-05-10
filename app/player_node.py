class PlayerNode:
    """node class used to store a player in a double linked list"""
    def __init__(self, player):
        self.__player = player
        self.__next = None
        self.__previous = None

    @property
    def player(self):
        """Return player object"""
        return self.__player

    @property
    def next(self):
        """Return next node"""
        return self.__next

    @next.setter
    def next(self, node):
        """Set next node"""
        self.__next = node

    @property
    def previous(self):
        """Return previous node"""
        return self.__previous

    @previous.setter
    def previous(self, node):
        """Set previous node"""
        self.__previous = node

    @property
    def key(self):
        """Return uid of the player"""
        return self.__player.uid

    def __str__(self):
        """Return string representation of the node"""
        return str(self.__player)
