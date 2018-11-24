def num_of_diff_comb(*args):
    ''' Return the number of different combinations using one entry from each provided set.'''
    c = 1
    for s in args:
        c *= len(s)
    return c

def count_strings(s: set, n: int, f: int = 0):
    '''Given a set of characters, return the number of different combinations of length n, and f being the number of character already determined in these cominations'''
    return len(s) ** (n-f)

def num_of_perms(n:int, r:int = 0) -> int:
    '''Return the number of permutations of size r'''
    if not r: r = n
    return fact(n) // fact(n-r)

def num_of_perms_2(n: int, r:int = 0) -> int:

    if not r: r = n

    res = 1
    for _ in range(r):
        res *= n
        n -= 1
    return res 

def seq_perms(s):
    return fact(len(s))

def num_of_combs(n: int, r: int = 0) -> int:
    '''Return the number of r-sized subsets'''
    if not r: r = n
    return fact(n) // (fact(r) * fact(n-r))


def fact(n: int):
    ''' Return the factorial of the given number'''
    return n * fact(n-1) if n else 1


def n_choose_r(n: int, r: int) -> int:
    '''Given n and r, return the number of ways to choose r from a set of size n.'''
    return fact(n) // (fact(r) * fact(n-r))