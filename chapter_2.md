# LESSON 2.7

## Prime Numbers

A number p is **prime** if it is an integer greater tha 1 and its only factors are 1 and p.

Conversely, a number is **composite** if it has a factor other tha 1 or itself.

Every positive integer greater than once can be expressed as a product of primes called its **prime factorization**.


## The Fundamental Theorum of Arithmatic
Every positive integer other than one can be expressed uniquely as a product of prime numbers where the prime factors are written in non-decreasing order.

**multiplicity** is the number of times a number appears in the product of primes:

120 = 2x2x2x3x5
multiplicity of 2 = 3
multiplicity of 3 = 1
mulitplicity of 5 = 1

Use exponential notation for a more compact presentation:
120 = 2^3 x 3 x5

# LESSON 2.8

**greatest common divisor (gcd)**
is the largest positive integer that is factor of both x and y (non-zero integers)

The largest number that divides the given numbers.

**least common multiple (lcm)**
is the smallest positive integer that is an integer multiple of both x and y ( non-zero integers)

The smallest number both given numbers can divide evenly.

Two numbers are said to be **relatively prime** if their greatest common divisor is 1.


24 = 2^3 * 3^1 * 5^0
50 = 2^1 * 3^0 * 5^2


gcd(24,50) = 2^min(3,1) *
             3^min(1,0) *
             5^min(0,2)
           = 2^1 * 3^0 * 5^0
           = 2

lcm(24,50) = 2^max(3,1) *
             3^max(1,0) *
             5^max(0,2)
           = 2^3 * 3^1 * 5^2
           = 600

# Brute Force Factorization

``` python

def brute_force_factoring:
    for x in range(2,n):
        if n % x:
            return "composite"
    return "prime"

```



rough likelyhood of hitting a prime number between 2 and x: 1/ln(x)


## Exercise 2.9.1

Use the prime number theorem to give an approximation for the number of prime numbers in the range 2 through 10,000,000.

1/ln(10000000)

