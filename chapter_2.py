from math import sqrt,log
import random
import sys

sys.setrecursionlimit(2000000)

def bf_is_prime(n: int) -> bool:
    ''' Brute force check if number is prime'''
    for x in range(2,n):
        if n % x == 0:
            return False
    return True

def bf_is_prime_2(n: int) -> bool:
    ''' Brute force check if number is prime, made more efficient by limiting check to the sqrt of n'''
    for x in range(2, int(sqrt(n))):
        if n % x == 0:
            return False
    return True

def fermat_is_prime(n: int) -> bool:
    if n == 2:      return True
    if not (n & 1): return False
    else:            return fast_modular_exponentation(2, n-1, n) == 1

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


def fast_modular_exponentation(x: int, y: int, n: int) -> int:
    '''Uses binary expansion to speed up the process of exponentation with modulo'''
    result: int = 1
    s: int = x
    r: int = y

    while r > 0:
        if r % 2 == 1:
            result = result * s % n
        s = s * s % n
        r = r // 2
    return result

def fast_exp(x: int, y: int, s: int = 0) -> int:
    '''Recursive implementation of fast exponentation algorithm'''
    s = s if s else x
    if y == 0:      return 1
    if y % 2:       return s * fast_exp(x, y//2, s*s)
    else:           return fast_exp(x, y//2, s*s)


# Modular Exponentation

def mod_exp(x: int, y: int, n: int, s: int = 0) -> int:
    '''Recursive implementation of modular exponentation algorithm'''
    s = s if s else x
    if y == 0:      return 1
    if x == 0:      return 0
    if y % 2:       return (s * mod_exp(x, y//2, n, s*s % n)) % n
    else:           return mod_exp(x, y//2, n, s*s % n)

assert(mod_exp(5,25,11) == (fast_exp(5,25) % 11))

# 5^68 mod 7
# binary expansion of 68: (1000100)
# 5^68 = 5^(2^6) * 5(2^2)
# 5^68 mod 7 = ((5^(2^6) mod 7) * (5(2^2) mod 7)) mod 7
# 5^68 mod 7 = (2*2) mod 7 = 4


def join_digits(input: list, digits_per: int):

    result = 0

    m: int = 1
    z: int =  10 ** digits_per

    for c in reversed(input):
        result += c * m
        m *= z

    return result



def generate_candidate() -> int: 
    # Generate Random Number
    r: int = random.getrandbits(1024)
    # Ensure Number is odd and the right length
    r |= 1
    r |= (1 << 1024)

    return r

def generate_large_prime_number() -> int:

    n: int = generate_candidate()

    while not fermat_is_prime(n):
        n = generate_candidate()
    
    return n


def create_rsa_keys() -> dict:

    p = generate_large_prime_number()
    q = generate_large_prime_number()

    N = p*q             # determine N
    phi = (p-1)*(q-1)     # determine phi

    # find integer e so that gcd(e,phi) == 1
    # e and phi must be relatively prime
    e = 459173

    # Find the multiplicative inverse of e % phi
    # An integer such that ed (mod z) == 1
    _,d,_ = egcd(e,phi)

    if d < 0:
        return create_rsa_keys()

    return {
        'N': N,
        'e': e,
        'd': d
    }

def encrypt(plaintext: str, keys: dict):
    ''' Using the RSA encryption scheme, encrypt the following message with the following public keys'''
    
    # c = m^e mod N
    msg: int = 0
    m: int = 1

    for c in reversed(plaintext):
        msg += ord(c) * m
        m *= 100

    return fast_modular_exponentation(msg, keys["e"], keys["N"])


def decrypt(ciphertext: int, keys: dict):
    ''' Using the RSA encryption scheme, decrypt the following message with the following public keys'''
    
    # m = c^d mod N
    value : int = fast_modular_exponentation(ciphertext, keys["d"], keys["N"])
    m: int = 100
    msg: list = []

    while value:
        msg.append(chr( value % m ))
        value //= m 

    return "".join(reversed(msg))




my_keys = create_rsa_keys()  

print(my_keys)

#print(encrypt('O', {'N': 1829, 'e': 859}))


encrypted_msg = encrypt('DA',my_keys)
decrypted_msg = decrypt(encrypted_msg, my_keys)

print(
    decrypted_msg
)

