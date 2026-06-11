from app.player_bnode import PlayerBNode


class PlayerBST:
    """binary search tree to store player objects."""

    def __init__(self):
        self.__root = None

    @property
    def root(self):
        """return root node of tree."""
        return self.__root

    def insert(self, player):
        """insert player into the binary tree search"""

        new_node = PlayerBNode(player)

        if self.__root is None:
            self.__root = new_node
        else:
            self.__insert_node(self.__root, new_node)

    def __insert_node(self, current_node, new_node):
        """find correct side for the new node"""

        current_name = current_node.player.name
        new_name = new_node.player.name

        # bigger names go to right side
        if new_name > current_name:

            if current_node.right is None:
                current_node.right = new_node
            else:
                self.__insert_node(current_node.right, new_node)

        # Smaller names go to left side
        elif new_name < current_name:

            if current_node.left is None:
                current_node.left = new_node
            else:
                self.__insert_node(current_node.left, new_node)

        # avoid duplicate if name already exists
        else:
            return

    def search(self, name):
        """search player by name"""

        current_node = self.__root

        while current_node is not None:

            current_name = current_node.player.name

            if name == current_name:
                return current_node.player

            elif name > current_name:
                current_node = current_node.right

            else:
                current_node = current_node.left

        return None

    def balance(self):
        """balance the binary search tree."""

        players = []

        self.__add_players_to_list(self.__root, players)

        self.__root = self.__build_balanced_tree(players)

    def __add_players_to_list(self, current_node, players):
        """add players to list in sorted order."""

        if current_node is None:
            return

        self.__add_players_to_list(current_node.left, players)

        players.append(current_node.player)

        self.__add_players_to_list(current_node.right, players)

    def __build_balanced_tree(self, players):
        """method to build a balanced tree from sorted players"""

        if len(players) == 0:
            return None

        middle_index = len(players) // 2
        middle_player = players[middle_index]

        new_node = PlayerBNode(middle_player)

        left_players = players[:middle_index]
        right_players = players[middle_index + 1:]

        new_node.left = self.__build_balanced_tree(left_players)
        new_node.right = self.__build_balanced_tree(right_players)

        return new_node