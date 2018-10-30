# RECURSION

def gen_arith(a: int, d: int):
    '''Arithmatic Sequence Function Factory: Consumes initial value, and common difference and returns recursive function which models that sequence'''
    def s(n: int) -> int:
        if n == 0:  return a
        else:       return d + s(n-1)
    return s

#by_three = gen_arith(0,3)

def gen_geo(a: int, r: int):
    '''Geometric Sequence Function Factory: Consumes initial value, and common ratio and returns a recursive function which models that sequence'''
    def s(n: int) -> int:
        if n == 0:  return a
        else:       return r * s(n-1)
    return s

#times_three = gen_geo(1,3)

def fib(n: int):
    ''' A recursive implementation of the Fibonacci Sequence'''
    if n == 0:      return 0
    if n == 1:      return 1
    else:           return fib(n-1) + fib(n-2) 

#9th_term = fib(9)

def rec_rel(a: int, f):
    '''Recurrance relation Generator: consumes intial value as well as function to represent all values past n == 0'''
    def s(n: int) -> int:
        if n == 0:  return a
        else:       return f(n,s)
    return s

# Using lambdas to generate sequences:
#by_three = rec_rel(0,lambda n,s: 3 + s(n-1))
#times_three = rec_rel(1, lambda n,s: 3 * s(n-1))
#fib_2 = rec_rel(0, lambda n,s: 1 if n == 1 else s(n-1) + s(n-2))
#assert(fib(10) == fib_2(10))

# SUMMATIONS

def seq_sum(s: int, n: int, f, k:int = 0):
    '''Consumes a lower limit (s), upper limit (n), function (f) and current term (k) and returns the sum of the given sequence'''
    k = k if k else s
    if k == n:  return f(k)
    else:       return f(k) + seq_sum(s,n,f,k+1)

'''
Practice Problems:

seq_sum(2,5, lambda k: 2*k -1)
seq_sum(0,2, lambda k: (k + 1)**2)
seq_sum(0,4,lambda k: 2**k),
seq_sum(0,200,lambda k: 2 + 3*k),
seq_sum(0,100,lambda k: 3 + 5*k),
seq_sum(0,100,lambda k: 3*(1.1)**k)

(7)Sigma(k=-2)(k^5)
(8)Sigma(k=2)(2^k)
(15)Sigma(k=1)(k^3)
(100)Sigma(k=0)((2k - 1)^2)

(18)Sigma(j=-2)(2^j) == (17)Sigma(j=-2)(2^j) + (2^18)
(n)Sigma(k=0)(k^2 - 4k + 1) == (n-1)Sigma(k=0)(k^2 - 4k + 1) + (n^2 -4n + 1)
(m+2)Sigma(k=0)(k^2 - 4k + 1) == (m+1)Sigma(k=0)(k^2 - 4k + 1) + (m+2)^2 - 4*(m+2) + 1

3 new cars per month, a0 = 23. Cars after 8 months (a8):
(8)Sigma(k=0)(23 + 3k) = 47
'''

def fac(n):
    return n* fac(n-1) if n else 1

def g(n):
    if n == 0:  return 0
    else:       return g(n-1) + n**3

def h(n):
    if n == 0:  return 1
    else:       return (n**2 + 1) * h(n-1)

def bin_set(n: int) -> set:
    ''' Given a length, n, return the set of all binary strings of that length.'''
    if n == 0:      return {''}
    else:           return  \
                    {i+b for i in bin_set(n-1) for b in ('1','0')}

def alpha_set(n: int) -> set:
    ''' Given a length, n, return the set of all lowercase alphabetical strings of that length'''
    if n == 0:      return {''}
    else:
        return \
        {i+chr(b) for i in alpha_set(n-1) for b in range(97,123)}

def rec_set(n: int, s: set) -> set:
    ''' Given a length, n, and a set,s, return the set of all strings with length n composed of the elements within s.'''
    if n == 0:      return {''}
    else:
        return \
        {i+x for i in rec_set(n-1,s) for x in s}

def perms(n: int, s: set) -> set:
    ''' Given a length, n, and a set, s, return a set of all permunations of the given with with length, s.'''
    if n == 0:      return {''}
    else:
        return \
        {i+x for i in perms(n-1,s) for x in s if not x in i}

class Node:
    ''' Simple Binary Tree Node'''
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
    def __str__(self, pre = "") -> str:
        res = pre + "<Node>\n"
        if self.left:
            res += self.left.__str__(pre+"    ")
        if self.right:
            res += self.right.__str__(pre+"    ")
        return res

def perf_bin_tree(n: int) -> Node:
    ''' Given an integer, n, return a perfect binary tree of that depth.'''
    if n == 1:      return Node()
    else:           return Node(perf_bin_tree(n-1),perf_bin_tree(n-1))