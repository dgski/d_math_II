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
    ''' Determine the decimal value of the given number'''
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


# Fast Exponentation
# Normally repeated multiplication is used, but that can be time consuming

# Example
# y = 53
# b^y = ?
# binary expansion of 53 = (110101)
# b^y = b^(1*2^5) * b^(1*2^4) * b^(0*2^3) * b^(1*2^2) * b^(0*2^1) * b^(1*2^0)
# b^y = b^(1*2^5) * b^(1*2^4) * b^(1*2^2) * b^(1*2^0)

def slow_exponentation(x: int, y: int) -> int:
    ''' A slow, iterative exponentation process'''

    if y == 0: return 1

    z: int = x
    while y > 1:
        z *= x
        y -= 1
    return z

# Manual Example
# 7 ^ 11
# binary expansion of 11: (1011)
# 7^11 = 7^(1*2^3) * 7^(0*2^2) * 7^(1*2^1) * 7^(1*2^0)
# 7^11 = 7^(1*2^3) * 7^(1*2^1) * 7^(1*2^0)
# # 7^11 = 7^8 * 7^2 * 7^1
# 7^11 = 5764801 * 49 * 7
# 7^11 = 1977326743

def fast_exponentation(x: int, y: int) -> int:
    '''Uses binary expansion to speed up the process of exponentation'''
    result: int = 1
    s: int = x
    r: int = y

    while r > 0:
        if r % 2 == 1:
            result *= s
        s *= s
        r = r // 2
    return result

def fast_exp(x: int, y: int, s: int = 1) -> int:
    '''Recursive implementation of fast exponentation algorithm'''
    if y == 0:      return 1
    if y % 2:       return (x**s) * fast_exp(x, y//2, s*2)
    else:           return fast_exp(x, y//2, s*2)

# Modular Exponentation
# ...