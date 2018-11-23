# Sum Rule

def num_of_diff_comb(*args):
    ''' Return the number of different combinations using one entry from each provided set.'''
    c = 1
    for s in args:
        c *= len(s)
    return c

def count_strings(s: set, n: int, f: int = 0):
    '''Given a set of characters, return the number of different combinations of length n, and f being the number of character already determined in these cominations'''
    return len(s) ** (n-f)

def pwd_combos()


def fact(n: int):
    ''' Return the factorial of the given number'''
    return n * fact(n-1) if n else 1


def n_choose_r(n: int, r: int) -> int:
    '''Given n and r, return the number of ways to choose r from a set of size n.'''
    return fact(n) // fact(r) * fact(n-r)