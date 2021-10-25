def is_leximin_better(x: list, y: list) -> bool:
    """
    return true iff x is leximin-better than y.

    >>> x = [4, 6, 4]
    >>> y = [5, 3, 5]
    >>> is_leximin_better(x, y)
    True
    >>> x = [4, 2, 4]
    >>> y = [5, 3, 2]
    >>> is_leximin_better(x, y)
    True
    >>> x = [1, 5, 5]
    >>> y = [5, 1, 5]
    >>> is_leximin_better(x, y)
    False
    >>> x = [4, 3, 2, 1, 0]
    >>> y = [9, 8, 7, 6, 5]
    >>> is_leximin_better(x, y)
    False
    >>> is_leximin_better(y, x)
    True
    >>> x = [1, 2]
    >>> y = [3, 2, 1]
    >>> is_leximin_better(y, x)
    Traceback (most recent call last):
        ...
    ValueError: len(x) must be equal to len(y)

    :rtype: bool
    """
    if len(x) != len(y):
        raise ValueError("len(x) must be equal to len(y)")
    while len(x) > 0:
        min_x = min(x)
        min_y = min(y)
        if min_x > min_y:
            return True
        elif min_x == min_y:
            x.remove(min_x)
            y.remove(min_y)
        else:
            return False
    return False


if __name__ == '__main__':
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
