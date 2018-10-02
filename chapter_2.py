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


def egcd(a, b):

    # ff a is zero, then by definition, x is zero and gcd is equal to b
    if(a == 0): return (b,0,1)
    
    q = b // a
    r = b % a
    
    # we are reaching to the future for these three values
    # g = will be found by using r as a and a as b
    # next_x = next_next_y - q * next_next_x
    # next_y = next_next_x
    # This will recur till the base case
    g, next_x, next_y = egcd(r, a)

    
    # gcd = ax + by
    # gcd = (b % a)(xn) + a(yn)
    x = next_y - q * next_x
    y = next_x

    print(
        "q = {} / {} = {}, r = {}, g = {}, x = {}, y = {}".format(b,a,q,r,g,x,y)
    )

    return (g, x, y)


print(
    egcd(675,210)
)