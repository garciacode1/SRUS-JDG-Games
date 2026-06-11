class PlayerBST:
    """binary search tree to store player objects."""

    def __init__(self):
        self.__root = None

    @property
    def root(self):
        """return root node of tree."""
        return self.__root