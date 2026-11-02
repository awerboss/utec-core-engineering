#!/usr/bin/env python3
"""Define a Square class with a custom string representation."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represent a square with a readable string representation."""

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(
            self._Square__size, self._Square__size
        )
