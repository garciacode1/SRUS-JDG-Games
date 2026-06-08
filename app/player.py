class Player:
    """Class player and attributes"""

    def __init__(self, uid, name, score=0):
        self.__uid = uid
        self.__name = name
        self.score = score

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0:
            raise ValueError("Score cannot be a negative value")
        self.__score = score

    def __repr__(self):
        """Return string representation."""
        return f"Player(name='{self.__name}', uid='{self.__uid}', score={self.__score})"

    @classmethod
    def calculate_hash(cls, key):
        """Return hash value for the key that was given."""
        total = 0

        for character in key:
            character_number = ord(character)
            total = total + character_number

        return total

    @classmethod
    def sort_quickly(cls, players):
        """Return players sorted by score in descending order."""

        if len(players) <= 1:
            return players

        pivot = players[len(players) // 2]
        left = []
        middle = []  #used as pivot
        right = []

        for player in players:
            if player.score > pivot.score:
                left.append(player)
            elif player.score < pivot.score:
                right.append(player)
            else:
                middle.append(player)

        return cls.sort_quickly(left) + middle + cls.sort_quickly(right)

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

    def __lt__(self, other):
        """Return True if this player score is less than the other player score."""
        return self.__score < other.score
