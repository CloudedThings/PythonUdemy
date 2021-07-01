def sum_eo(number, string):
    if string == 'e':
        start = 2
    elif string == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, number, 2))

