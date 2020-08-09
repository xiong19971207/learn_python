def _sort(_list):
    for j in range(len(_list) - 1):
        for i in range(len(_list) - 1):
            if _list[i] > _list[i + 1]:
                _list[i], _list[i + 1] = _list[i + 1], _list[i]

    return _list


a = [98, 5, 9, 44, 11, 77, 88, 99, 22, 15, 64, 78]
print(_sort(a))
