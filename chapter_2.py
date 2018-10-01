from math import sqrt

def bf_is_prime(n: int) -> bool:
    ''' Brute force check if number is prime'''
    for x in range(2,n):
        if n % x == 0:
            return False
    return True

def bf_is_prime_2(n: int) -> bool:
    ''' Brute force check if number is prime, made more efficient by limiting check to the sqrt of n'''
    for x in range(2,int(sqrt(n))):
        if n % x == 0:
            return False
    return True


def find_gcd(x: int, y: int) -> int:
    ''' Uses Euclid's algorithm to determine the greatest common denominator. '''
    if y < x:
        x,y = y,x

    r: int = y % x

    while r != 0:
        y = x
        x = r
        r = y % x

    return x


def gcd(a,b):
    '''Recursive application of Euclid's algorithm'''
    return a if (b % a == 0) else gcd(b % a, a)