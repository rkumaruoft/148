from __future__ import annotations
from typing import Any, Optional


class BinarySearchTree:
    """Binary Search Tree class."""
    # === Private Attributes ===
    # The item stored at the root of the tree, or None if the tree is empty.
    _root: Optional[object]
    # The left subtree, or None if the tree is empty
    _left: Optional['BinarySearchTree']
    # The right subtree, or None if the tree is empty
    _right: Optional['BinarySearchTree']

    # === Representation Invariants ===
    # - If _root is None, then so are _left and _right.
    # This represents an empty BST.
    # - If _root is not None, then _left and _right are BinarySearchTrees.
    # - (BST Property) All items in _left are <= _root,
    # and all items in _right are >= _root.
    def __init__(self, root: Optional[object]) -> None:
        """Initialize a new BST with the given root value.
        If <root> is None, the tree is empty, and the subtrees are None.
        If <root> is not None, the subtrees are empty.
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def is_empty(self) -> bool:
        """Return True if this BST is empty.
        """
        return self._root is None

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this BST.

        >>> bst = BinarySearchTree(3)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> 3 in bst
        True
        >>> 5 in bst
        True
        >>> 2 in bst
        True
        >>> 4 in bst
        False
        """
        if self.is_empty():
            return False
        elif item == self._root:
            return True
        elif item < self._root:
            return item in self._left  # or, self._left.__contains__(item)
        else:
            return item in self._right  # or, self._right.__contains__(item)

    def items(self) -> list:
        """Return all the items in the BST in sorted order.

        You should *not* need to sort the list yourself: instead, use the BST
        property and combine self._left.items() and self._right.items()
        in the right order!

        >>> BinarySearchTree(None).items()  # An empty BST
        []
        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.items()
        [2, 3, 5, 7, 9, 11, 13]
        """
        if self.is_empty():
            return []
        else:
            return self._left.items() + [self._root] + self._right.items()

    def __str__(self) -> str:
        """Return a string representation of this BST.

        This string uses indentation to show depth.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this BST.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            answer = depth * '  ' + str(self._root) + '\n'
            answer += self._left._str_indented(depth + 1)
            answer += self._right._str_indented(depth + 1)
            return answer

    def delete(self, item: object) -> None:
        """Remove *one* occurrence of item from this BST.
        Do nothing if <item> is not in the BST.
        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.items()
        [2, 3, 5, 7, 9, 11, 13]
        >>> bst.delete(2)
        >>> bst.items()
        [3, 5, 7, 9, 11, 13]
        >>> bst.delete(9)
        >>> bst.items()
        [3, 5, 7, 11, 13]
        """
        if self.is_empty():
            return None
        elif self._root == item:
            self.delete_root()
        elif self._root < item:
            self._right.delete(item)
        else:
            self._left.delete(item)

    def delete_root(self) -> None:
        if self._left.is_empty() and self._right.is_empty():
            self._root = None
            self._left = None
            self._right = None
        elif self._left.is_empty():
            # Promote the right tree
            this = self._right
            self._root = this._root
            self._left = this._left
            self._right = this._right
        elif self._right.is_empty():
            # Promote the left tree
            this = self._left
            self._root = this._root
            self._left = this._left
            self._right = this._right
        else:
            self._root = self._right.delete_helper()

    def delete_helper(self) -> Any:
        if self._left.is_empty():
            min_ = self._root
            self.delete_root()
            return min_
        else:
            return self._left.delete_helper()

    
