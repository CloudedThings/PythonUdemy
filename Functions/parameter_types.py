def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("Keyword:.................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)

def sum_numbers(*i: float) -> float:
    """
    Summarize a provided number
    :param i: proviaded values
    :return: sum of the value
    """
    return sum(i)