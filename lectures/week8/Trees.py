from __future__ import annotations
from typing import Any, Callable, Optional, List, Union


class Tree:
    """A recursive tree data structure.
    """

    # === Private Attributes ===
    # The item stored at this tree
    # === Representation Invariants ===
    # - If self._root is None then self._subtrees is an empty list.
    # This setting of attributes represents an empty tree.
    #
    # Note: self._subtrees may be empty when self._root is not None.
    # This setting of attributes represents a tree consisting of just one
    # node.
    _root: Optional[Any]
    _subtrees: list[Tree]

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.
        If <root> is None, the tree is empty.
        Precondition: if <root> is None, then <subtrees> is empty.
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty.
        """
        return self._root is None

    def leaves(self) -> list:
        """Return a list of all of the leaf items in the tree.
        >>> Tree(None, []).leaves()
        []
        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> t.leaves()
        [2, 5]
        """
        if self.is_empty():
            return []

        if not self._subtrees:
            return [self._root]
        else:
            leaves = []
            for tree in self._subtrees:
                leaves.extend(tree.leaves())
            return leaves

    def average(self) -> float:
        """Return the average of all the values in this tree.
        Return 0.0 if this tree is empty.
        Precondition: this is a tree of numbers.
        >>> Tree(None, []).average()
        0.0
        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> round(t.average(),2)
        2.67
        >>> t = Tree(1, [Tree(2, []), Tree(5, [Tree(2, [])])])
        >>> round(t.average(),2)
        2.5
        """
        total, count = self.average_helper()

        if count == 0:
            return 0.0
        else:
            return total / count

    def average_helper(self) -> tuple[float, int]:
        """

        """
        if self.is_empty():
            return 0.0, 0

        if not self._subtrees:
            return self._root, 1
        else:
            count = 1
            total = self._root
            for tree in self._subtrees:
                this_total, this_count = tree.average_helper()
                count += this_count
                total += this_total
            return total, count

    def preorder(self) -> str:
        """
        >>> t = Tree(1, [Tree(2, []), Tree(5, [Tree(2, [])])])
        >>> t.preorder()
        '1 2 5 2'
        """
        #
        # if self.is_empty():
        #     return ''
        # else:
        #     s = str(self._root)
        #     for tree in self._subtrees:
        #         s =

    def delete_item(self, item: Any) -> bool:
        """
        Delete *one* occurrence of item in the tree
        """
        if self.is_empty():
            return False
        elif self._subtrees == []:
            if self._root != item:
                return False
            else:
                self._root = None
                return True
        else:
            if self._root == item:
                # self._delete_root()
                return True
            else:
                for sub_tree in self._subtrees:
                    if sub_tree.delete_item(item):
                        return True
                return False

    def _delete_root_promote(self) -> none:
        """


        """

        to_promote = self._subtrees.pop()
        self._root = to_promote._root
        self._subtrees.extend(to_promote._subtrees)

    def _delete_root_leaf(self) -> Optional[Any]:
        """
        """
        if self._subtrees == []:
            ret_val = self._root
            self._root = None
            return ret_val
        else:
            for sub in self._subtrees:
                x = sub._delete_root_leaf()
                if x is not None:
                    return x
            old = self._root
            self._root = None
            self._subtrees = []
            return old

    def to_nested_lst(self) -> list:
        if self.is_empty():
            return []
        else:
            if self._subtrees == []:
                return [self._root]
            else:
                ret_lst = [self._root]
                for sub_tree in self._subtrees:
                    ret_lst.append(sub_tree.to_nested_lst())
                return ret_lst


def to_tree(obj: int | list) -> Optional[Tree]:
    if isinstance(obj, int):
        return None
    else:
        root = obj[0]
        subtrees = []
        for i in obj[1:]:
            subtrees.append(to_tree(i))

    return Tree(root, subtrees)

