def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    """Return the most occurred element in the list"""
    dict = {}
    for num in nums:
        dict[num] = dict.get(num, 0) + 1
    max_value = max(dict.values())
    modes = [k for k, v in dict.items() if v == max_value]
    return modes