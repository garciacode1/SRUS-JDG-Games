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

    def __str__(self):
        """string method to return readable string ->player object"""
        return f"Player: {self.__name}, Unique id: {self.__uid}"
