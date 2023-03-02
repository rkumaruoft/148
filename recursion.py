from typing import List, Optional, Union


def flatten(obj: Union[int, List]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>.
    The integers are returned in the left-to-right order they appear
    in <obj>.
    >>> flatten(6)
    [6]
    >>> flatten([1, [-2, 3], -4])
    [1, -2, 3, -4]
    >>> flatten([[0, -1], -2, [[-3, [-5]]]])
    [0, -1, -2, -3, -5]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
    for sublist in obj:
        s.extend(flatten(sublist))
    return s


def uniques(obj: Union[int, List]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>, with no duplicates.
    >>> uniques([13, [2, 13], 4])
    [13, 2, 4]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
        for sublist in obj:
            u = uniques(sublist)
            for i in u:
                if i not in s:
                    s.append(i)
        return s


def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """Return whether the given item appears in <obj>.
    Note that if <obj> is an integer, this function checks whether
    <item> is equal to <obj>.
    >>> nested_list_contains(4, 4)
    True
    >>> nested_list_contains([1, [2, [3, 4], 5] , [6]], 4)
    True
    >>> nested_list_contains([1, [2, [3, 4], 5] , [6]], 9)
    False
    """
    if isinstance(obj, int):
        return obj == item
    else:
        for sub_lst in obj:
            if nested_list_contains(sub_lst, item):
                return True
        return False


def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """
    Return the first (leftmost) item in <obj> at depth <d>.
    Return None if there is no item at depth <d>.
    Precondition: d >= 0.
    >>> first_at_depth(2, 0)
    2
    >>> first_at_depth(2, 3)

    >>> first_at_depth([1, [2, 3], 4], 2)
    2
    """
    if d == 0:
        return obj
    elif isinstance(obj, int):
        return None
    else:
        for sublist in obj:
            i = first_at_depth(sublist, d - 1)
            if i is not None:
                return i
        return None


def add_one(obj: Union[int, List]) -> None:
    """Add one to every number stored in <obj>. Do nothing if <obj> is an int.
    If <obj> is a list, *mutate* it to change the numbers stored.
    >>> lst0 = 1
    >>> add_one(lst0)
    >>> lst0
    1
    >>> lst1 = []
    >>> add_one(lst1)
    >>> lst1
    []
    >>> lst2 = [1, [2, 3], [[[5]]]]
    >>> add_one(lst2)
    >>> lst2
    [2, [3, 4], [[[6]]]]
    """
    if not isinstance(obj, int):
        for i in range(len(obj)):
            if isinstance(obj[i], int):
                obj[i] += 1
            else:
                add_one(obj[i])
