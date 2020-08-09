def quick_sort(_list):
    if len(_list) <= 1:
        return _list
    else:
        first = _list[0]
        left = [x for x in _list[1:] if x <= first]
        right = [x for x in _list[1:] if x > first]
    return quick_sort(left) + [first] + quick_sort(right)


a = [99, 88, 77, 55, 66, 44, 11, 22, 33]
print(quick_sort(a))
