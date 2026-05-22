class Player:
    """Class player and attributes"""
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @classmethod
    def calculate_hash(cls, key):
        """Return hash value for the key that was given."""
        total = 0

        for character in key:
            character_number = ord(character)
            total = total + character_number

        return total

    def __hash__(self):
        """Return hash value for the player."""
        return self.calculate_hash(self.__uid)

    def __eq__(self, other):
        """Return True if two players use same uid."""
        if not isinstance(other, Player):
            return False

        return self.__uid == other.uid

    def __str__(self):
        """string method to return readable string ->player object"""
        return f"Player: {self.__name}, Unique id: {self.__uid}"
