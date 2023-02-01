from typing import Any
from copy import deepcopy, copy

class Stack:
    """A last-in-first-out (LIFO) stack of items.
    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.
    """
    # === Private Attributes === _items: The items stored in this stack. The
    # end of the list represents the top of the stack.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack."""

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push(
        hello
        )
        >>> s.is_empty()
        False
        """

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack.
        """

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.
        >>> s = Stack()
        >>> s.push(
        hello
        )
        >>> s.push(
        goodbye
        )
        >>> s.pop()

        goodbye
        """


def size(s: Stack) -> int:
    """Return the number of items in s.
    """
    s_copy = copy(s)
    # count = 0
    # while not s_copy.is_empty():
    #     s_copy.pop()
    # count += 1
    # return count
    print(id(s))
    print(id(s_copy))


if __name__ == '__main__':
    stack = Stack()
    size(stack)
