class Jar:
    _size = 0

    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return ("🍪" * self._size)

    def deposit(self, n):
        self.size = n

    def withdraw(self, n):
        self.size = -n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies")
        elif self._size + n < 0:
            raise ValueError("Not enough cookies")
        else:
            self._size += n