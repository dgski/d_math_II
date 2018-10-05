from math import sqrt,log

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

def gcd(a: int, b: int) -> int:
    '''Recursive application of Euclid's algorithm'''
    return a if (b % a == 0) else gcd(b % a, a)

def egcd(a: int, b: int) -> tuple:

    # ff a is zero, then by definition, x is zero and gcd is equal to b
    if(a == 0): return (b,0,1)
    
    q: int = b // a
    r: int = b % a
    
    # we are reaching to the future for these three values
    # g = will be found by using r as a and a as b
    # next_x = next_next_y - q * next_next_x
    # next_y = next_next_x
    # This will recur till the base case
    
    g, next_x, next_y = egcd(r, a)
    
    # Why the following works:
    # let (xn): next_x, (yn): next_y
    # gcd = ax + by
    # gcd = (b % a)(xn) + a(yn)
    # therefore: 
    # (b % a)(xn) + a(yn) = ax + by
    # (b - (b//a)*a)(xn) + a(yn) = ax + by
    # b(xn) - ((b//a)*a)(xn) + a(yn) = ax + by
    # b(xn) - a(b//a)(xn) + a(yn) = ax + by
    # b(xn) + a(-(b//a)(xn) + yn) = ax + by
    # therefore:
    # y = xn
    # and:
    # x = -(b//a)(xn) + yn
    
    x: int = next_y - q * next_x
    y: int = next_x

    return (g, x, y)

def find_mul_inverse(a: int,b: int) -> int:
    '''Determine the multiplicative inverse of a % b'''
    return egcd(a,b)[1] % b

def dec_value(digits: list, base: int) -> int:
    ''' Determine the decimal of the given number'''
    res: int = 0
    power: int = len(digits) - 1
    
    for n in digits:
        res += n * (base ** power)
        power -= 1

    return res

def conv_dec_to_base(n: int, b: int) -> str:
    ''' Convert the given decimal value to the given base'''
    res: list = []
    x: int = n
    
    while x > 0:
        res.append(str(x % b))
        x = x // b

    res.reverse()

    return "".join(res)

def digits_in_integer(n: int, b: int) -> int:
    ''' Determine the number of digits in given dec integer with the given base'''
    return round(log((n -1),b))