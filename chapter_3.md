# Recursion

## Recurance Relation defined by an arithmetic sequence
a0 = a (initial value)
an = d + a(n-1) for n >= 1 (recurrence relation)
a = intial value, d = common difference

## Geometric Sequence
a0 = a (intial value)
an = r*a(n-1) for n >= 1 (recurrance relation)
a = intial value, r = common ratio

## Fibonacci Sequence
f0 = 0
f1 = 1
fn = f(n-1) + f(n-2) for n >= 2

# Summations

**a_seq:**
a(s), a(s+1), a(s+2), ... , a(n)

**Sum(a_seq):**
(n)Sigma(k=s) = a(s) + a(s+1) + a(s+2), + , a(n)
s = lower limit
n = upper limit

**nth partial sum:**
(n)Sigma(k=1)
nth term = S(n) - S(n-1)

Summation Notation can be used to sum up the terms in a sequence defined by an explicit formula:

ak = k^3, for k = 1,2,3,4

(4)Sigma(k=1) = 1^3 + 2^3 + 3^3 + 4^3 = 100

|-----------|   |-------------------------|
summation form      expanded form

**Remember:**
**(n)Sigma(j=1)(j+1) != (n)Sigma(j=1)j+1**

## Pulling Out Final Term

(n)Sigma(k=m)ak == (n-1)Sigma(k=m)ak + an

## Change of Variables in Summation

**Consider the following:**
(n)Sigma(k=1)((k+2)^3)
**Substituting i = k + 2**
1. Determine new lower limit:
    k = 1
    i = k + 2
    i = 1 + 2
    i = 3
2. Determine new upper limit:
    k = n
    i = k + 2
    i = n + 2
3. Replace the variables in the terms
    i = k + 2
    k = i - 2
    ((i-2)+2)^3
    i^3

= (n+2)Sigma(i=3)(i^3)