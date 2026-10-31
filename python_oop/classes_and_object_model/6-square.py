
#!/usr/bin/env python3
"""Define a square with size, position and string representation."""


class Square:
    """Represent a square with a size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and update the size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and update the position."""
        if (type(value) is not tuple or len(value) != 2
                or type(value[0]) is not int
                or type(value[1]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError(
    "position must be a tuple of 2 positive integers"
)
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using its position."""
        print(self)

    def __str__(self):
        """Return the square as a formatted string."""
        if self.__size == 0:
            return ""

        lines = [""] * self.__position[1]

        for _ in range(self.__size):
            lines.append(" " * self.__position[0]
                         + "#" * self.__size)

        return "\n".join(lines)
