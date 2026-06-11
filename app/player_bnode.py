class PlayerBNode:
    """Node class created to store a player in a Binary Search Tree."""

    def __init__(self, player):
        self.__player = player
        self.__left = None
        self.__right = None

    @property
    def player(self):
        """return player object"""
        return self.__player

    @property
    def left(self):
        """return left child node"""
        return self.__left

    @left.setter
    def left(self, node):
        """Set left child node"""
        self.__left = node

    @property
    def right(self):
        """return right child node"""
        return self.__right

    @right.setter
    def right(self, node):
        """Set right child node"""
        self.__right = node

