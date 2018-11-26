# Counting

In Discrete Mathematics the goal is to count the number of elements in (of the cardinality of) a finite set given a description of the set.

**cardinality:** number of elements of

## The Product Rule

Let A1,A2,...,An be finite sets. Then,
|A1 * A2 *...*An| = |A1| * |A2| *...*|An|

### Counting Strings

If E is a set of chracters(called an alphabet) then E^n if the set of all strings of length n whose characters come from the set E.

if E = {'A','B'}, then E^3 is a set of all strings with 3 letters.

The string 'ABA' is an example element in E^6.

**The product rule can be applied directly to determine the number of strings of a given length of a finite alphabet:**

            ntimes          ntimes
        ______________   _________________
|E^n| = |E * E *...*E| = |E| * |E| *...|E| = |E|^n

**You can also use it when one or more of the characters are fixed:**

Example: B*B
|S| = |{'B'} * {'A','B'} * {'B'}| =  1*2*1 = 2

## The Sum Rule

Consider the sets A1,A2,...,An, If the sets are mutually disjoint(Ai n Aj = (/) for i != j), then |A1 u A2 u...u An| = |A1| + |A2| +...+ |An|

H = {coffee, hot cocoa, tea}
C = {milk, orange juice}
|H u C| = |H| + |C|
        = 3 + 2
        = 5

## Bijection

Given two sets S,T. If a function,f maps S onto T, then there exists a function g, which maps T onto S such that:
f(s) = t
g(t) = s

**Formal:**
f(Y) = y <-> f^-1(y) = Y

## K-to-1 correspondence

Let X and Y be finite sets. The function f:X->Y is a k-to-1 correspondence if for every yEY, there are exactly k different x E X such that f(x) = y

f(can_id) = pack_id

## The generalized product rule

|S| = n1 * n2 * nk

# Permutations and Combinations

**permutations**: arrangements

**r-permutation**: permutation of a subset
"permutations of n things taken r at a time"

permutations: order matters
combinations: order does not matter

## The number of r-permutations from a set with n elements

P(n,r) = n * (n-1)...(n-r+1) = n!/(n-r)!

**Ex:**
P(n,3) = n * (n-1) * (n-2)
P(4,3) = 3 * (3-1) * (3-2)
       = 4 * 3 * 2
       = 24

## The number of permuations of a set

P(n) = n!

## The number of r-subset (combinations)

C(n,r) = n! / r! * (n-r)!

## Summary

P(n,n) = n!
P(n,r) = n! // (n-r)!
C(n,r) = n! // r! *  (n-r)!

# Counting Subsets

(n) = n choose r
(r)

(n) == (n  )
(r)    (n-r)

# Permutations With Repitition

If a sequence has items that repeat, you must apply the formulta for counting permutations with repetition:

**Example:**

How many ways to scramble **MISSISSIPPI**?

P: 11 choose 2
I: 9 choose 4
S: 5 choose 4
M: 1 choose 1

= (11! / 2!9!) * (9!/ 4!5!) * (5! / 4!1!) * (1! / 1!0!)
= 11! / 2!4!4!1!

# Counting By Complement
             _
|P| = |S| = |P|

# Multisets

A **multiset** is a collection that can have multiple instances of the same kind of item. Just as with sets, order of the elements does matter.

## Formula

(n + m - 1)
(m - 1)

(n + m -1)! / (m-1)!n!

n = number of objects
m = the number of varieties of objects

# Generating permutations and combinations

**n-tuple** is an ordered st of n items.
**permutations** are sets,sequences, or series where order matters.
**combinations** are subsets where order does not matter.

(1,2) > (1,1)

To generate the permutations of a given set. Generate the first sequence in lexographic order, and continually generate the next one, until you generate the last one.

Generate: (1,2,3) to (3,2,1)

To generate the r-subsets of a given set. Generate the first set in lexographic order (Using the absolute smallest elements) and continually generate the next one until you generate the last one (absolute largest elements).

Using {1,2,3,4,5}

Generate: {1,2,3} to {3,4,5}


## Recursive generation of Permutations

[1,2,3] ->  [1] + perms([2,3]),
            [2] + perms([1,3]),
            [3] + perms([1,2])

# Advanced Counting Techniques

# Inclusion-Exclusion principle

Let A and B be two finite sets, then |A u B| = |A| + |B| - |A n B|

For three sets: |A u B u C| = |A| + |B| + |C| - |A n N| - |B n C| - |A n C| + |A n B n C|

A collection of sets is **mutually disjoint** if the intersection of any pairs of sets in the collection is empty.

| A1 u A2 u...u An | = |A1| + |A2| +...+ |An|

**Ex:** (33*4) - (18* n_choose_r(4,2)) + (11*n_choose_r(4,3)) -3