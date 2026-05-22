from app.player import Player
from app.player_list import PlayerList


class PlayerHashMap:
    """Hash map used for storing players using PlayerList chaining."""

    SIZE = 10

    def __init__(self):
        self.__hashmap = [PlayerList() for _ in range(self.SIZE)]
        self.__size = 0

    def get_index(self, key) -> int:
        """Return hash map index for the given key."""
        return Player.hash(key) % self.SIZE