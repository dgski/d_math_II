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

def num_of_perms_in_string(s: str) -> int:
    '''Return the number of ways to permute the characters in a string'''
    l = {}
    for c in s:
        if c in l:
            l[c] += 1
        else:
            l[c] = 1
    
    num = len(s)
    den = 1
    for _,v in l.items():
        den *= fact(v)
    return fact(num) // den


def count_multisets(l: list) -> int:
    s = set(l)
    n = len(l)
    m = len(s)
    return  n_choose_r(n + m - 1, m-1)

def count_multisets_2(n: int, m: int) -> int:
    return n_choose_r(n + m - 1, m-1)

def next_perm(p):
    n = list(p)
    x = 0

    i = len(n) - 1
    while 0 < i:
        if((n[i-1]) < n[i]):
            x = i-1
            break
        i -= 1

    swap = n.index(min((i for i in n[x+1:] if i > n[x])))

    n[swap],n[x] = n[x],n[swap]
    return n[:x+1] + sorted(n[x+1:])

def gen_perms(n):
    perms = []
    p,e = list(range(n)),list(reversed(range(n)))
    perms.append(p)

    while p != e:
        p = next_perm(p)
        perms.append(p)

    return perms

def gen_perms_rec(s):
    if len(s) == 2: return [s,[s[1],s[0]]]
    else:           return [[s[i]] + x for i in range(len(s)) for x in gen_perms_rec(s[:i]+s[i+1:])]

def next_subset(n,s):
    f = list(s)
    n = list(range(1,n+1))
    x = 0
    for i in range(1,len(f)+1):
        if f[-i] < n[-i]:
            x = len(f)-i
            break
    f[x] += 1
    x += 1

    while x < len(f):
        f[x] = f[x-1] + 1
        x += 1

    return f

def gen_lex_subsets(r,n):
    subsets = []
    s = list(range(1,r+1))
    f = list(range(n-r+1,n+1))
    subsets.append(s)

    while s != f:
        s = next_subset(n,s)
        subsets.append(s)
    return subsets

def gen_div_by(d,n):
    i = 1
    while i <= n:
        if i % d == 0:
            yield i
        else:
            yield 0
        i += 1

def find_common_235():
    u = 0
    for i,j,k in zip(   gen_div_by(2,30),   \
                        gen_div_by(3,30),   \
                        gen_div_by(5,30)    ):

        if i and j and k:   u += 1
        if i and j:         u -= 1
        if i and k:         u -= 1
        if j and k:         u -= 1
        if i:               u += 1
        if j:               u += 1
        if k:               u += 1

    return u

def divisible_by(n,a,b,c):
    u = 0
    for i,j,k in zip(   gen_div_by(a,n),   \
                        gen_div_by(b,n),   \
                        gen_div_by(c,n)    ):
        if i and j and k:   u += 1
        if i and j:         u -= 1
        if i and k:         u -= 1
        if j and k:         u -= 1
        if i:               u += 1
        if j:               u += 1
        if k:               u += 1
    return u