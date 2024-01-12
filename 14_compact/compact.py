def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_list = []
    for element in lst:
        if element:
            new_list.append(element)
    return new_list

    # return [element for element in lst if element]