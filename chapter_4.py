
def fact(n: int):
    ''' Return the factorial of the given number'''
    return n * fact(n-1) if n else 1


def n_choose_r(n: int, r: int) -> int:
    '''Given n and r, return the number of ways to choose r from a set of size n.'''
    return fact(n) // fact(r) * fact(n-r)