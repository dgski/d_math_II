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

## Closed Forms of Summations

**Arithmatic Sequence:**
(n-1)Sigma(k=0)(a + ak) = an + (d(n-1) * n)/2

**Geometric Sequence**
(n-1)Sigma(k=0)(a*r^k) = a(r^n - 1)/(r - 1)

## Induction

An inductive proof establishes that some statement parameterized by n is true, for any positive integer n.

1. **Base Case**
2. **Inductive Step**

1. Q(1) is true
2. Q(k) implies Q(k+1)

## Inductive proof of a recurrence relation

**Define the Sequence as:**

h(0) = 7
h(n) = (h(n-1))^3

**Then for any n >= 0:**

h(n) = 7^(3^n)

**Proof**

By induction on n.

**Base Case**

We must show that n(0) = 7^(3^0)
Since 7 = 7^(1), the theorum holds for n(0).

**Inductive Step**

Supposed that for any integer k >= 0,
h(k) = 7^(3^k), Then we will show that:
h(k+1) =  7^(3^(k+1))

h(k+1) = h((k+1)-1)^3
       = h(k)^3
       = (7^(3^k))^3
       = (7^3*(3^k))
       = 7^(3 * 3^k)
       = 7^(3^(k+1))

Therefore h(k+1) = 7^(3^n)

## Strong Induction

**Base Case**

S(a),S(a+1),...,S(b) are true

**Inductive Step**

For all k => b, if 
S(a) ^ S(a+1)^,...,^S(k) is true then S(k+1) is also true

## Well-ordering principle

**well-ordering principle** says that any non-empty subset of the non-negative integers has a smallest element.

## Recursive Sets
B^k, where B={0,1} is the set of all binary strings of length k.
B^* is the set of all binary strings with no length restriction.
lambda - is the empty string whose length is zero.
B^0 is the lenghth of all binary strings of length 0, therefore B^0 - {lambda}

**B^* can be defined as an infinite union:**

B^* = B^0 u B^1 u B^2 u ...

**Or recursively:**

base case: lambda is an element of B^*
recursive rule: if x is an element of B^* then x0 is an element of B^*
, x1 is an element of B^*.

**Components of a recursive definition of a set**
1. A basis states that one of more specifix elements are in the set.
2. A recursive rule shows how to construct larger elements in the set from elements already know to be in the set.
3. An exclusion statement staest hat an element is in the set only if it is given in the basis or can be built by applying the recursive rules repeatedly to elements given in the basis.