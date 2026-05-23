from app.player import Player
from app.player_list import PlayerList


class PlayerHashMap:
    """Hash map used for storing players using PlayerList chaining."""

    SIZE = 10
    
    def __init__(self):
        self.__hashmap = [PlayerList() for _ in range(self.SIZE)]
        self.__size = 0

    def get_index(self, key):
        """Return hash map index for the given key."""
        if isinstance(key, Player):
            return hash(key) % self.SIZE

        return Player.calculate_hash(key) % self.SIZE

    def put(self, key, name):
        """Add or update a player in the hash map."""

        hash_index = self.get_index(key)
        selected_list = self.__hashmap[hash_index]

        node_to_check = selected_list.head

        while node_to_check is not None:

            if node_to_check.key == key:
                node_to_check.player.name = name
                return

            node_to_check = node_to_check.next

        player = Player(key, name)
        selected_list.insert_tail(player)
        self.__size += 1

    def get(self, key):
        """Return player with the matching key."""

        hash_index = self.get_index(key)
        selected_list = self.__hashmap[hash_index]

        node_to_check = selected_list.head

        while node_to_check is not None:

            if node_to_check.key == key:
                return node_to_check.player

            node_to_check = node_to_check.next

        return None

    def remove(self, key):
        """Remove player with the matching key."""

        hash_index = self.get_index(key)
        player_list_at_index = self.__hashmap[hash_index]

        deleted_node = player_list_at_index.delete_item_by_key(key)

        if deleted_node is not None:
            self.__size -= 1
            deleted_player = deleted_node.player
            return deleted_player

        return None

    def size(self):
        """Return number of players in the hash map."""
        return self.__size

    def display(self):
        """Display all non-empty player lists in the hash map."""

        for index, selected_list in enumerate(self.__hashmap):

            if not selected_list.is_empty:
                print(f"Index {index}:")
                selected_list.display()