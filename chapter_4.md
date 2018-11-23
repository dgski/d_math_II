# Counting

In Discrete Mathematics the goal is to count the number of elements in (of the cardinality of) a finite set given a description of the set.

**cardinality:** number of elements of

## The Product Rule

Let A1,A2,...,An be finite sets. Then,
|A1 * A2 *...*An| = |A1| * |A2| *...*|An|

### Counting Strings

If E is a set of chracters(called an alphabet) then E^n if the set of all strings of length n whose characters come from the set E.

if E = {'A','B'}, then E*3 is a set of all strings with 3 letters.

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