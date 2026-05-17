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

    def delete_item_from_head(self):
        """delete player from head of list"""

        if self.is_empty:
            return None

        removed_node = self.__head

        if self.__head != self.__tail:
            self.__head = self.__head.next
            self.__head.previous = None
        else:
            self.__head = None
            self.__tail = None

        return removed_node

    def delete_item_from_tail(self):
        """delete item from tail of list"""

        if self.is_empty:
            return None

        removed_node = self.__tail

        if self.__head != self.__tail:
            self.__tail = self.__tail.previous
            self.__tail.next = None
        else:
            self.__head = None
            self.__tail = None
        return removed_node

    def delete_item_by_key(self, key):
        """Delete player by key from list"""

        current_node = self.__head

        while current_node is not None:

            if current_node.key == key:

                if current_node == self.__head:

                    if self.__head == self.__tail:
                        self.__head = None
                        self.__tail = None

                    else:
                        self.__head = self.__head.next
                        self.__head.previous = None

                elif current_node == self.__tail:

                    self.__tail = self.__tail.previous
                    self.__tail.next = None

                else:

                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                return current_node

            current_node = current_node.next
        return None

    def display(self, forward=True):
        """Display linked list"""

        # Display from head to tail
        if forward:

            print("Displaying list from head to tail:")

            current_node = self.__head

            while current_node is not None:
                print(current_node)

                current_node = current_node.next

        # Display from tail to head
        else:

            print("Displaying list from tail to head:")

            current_node = self.__tail

            while current_node is not None:
                print(current_node)

                current_node = current_node.previous
