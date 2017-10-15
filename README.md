# pypnunum
Gustafson Unum 2.0 written in Python 3.5

This is started with inspiration from this Julia version https://github.com/jwmerrill/Pnums.jl

See also my C++ version of the same https://github.com/eruffaldi/cppunum2

# Approach

The Alphabet class stores the alphabet of the lattices with only the exact values >= 1, always starts with 1, and length power of 2. Given the alphabet of size N we obtain an unum of size 8N, that is if the generators are N=2^k we obtain an unum of 2^(k+3) bits. Each generator on the lattice is associated with 4 exact points: x 1/x -x -1/x except for 1. All these points are efficiently accessible.

Punum is a number expressed as an index over the lattice wheel with a link to the Alphabet

Summation and products require tables, so the gentable script is the first step in generating these tables, otherwise operations are implemented via their numeric counterpart: that is convert to fractions, compute the result and then find the nearest point on the lattice wheel. 

A- full: 8n 8n = 64n^4
B- sym: 8n  (8n+1)/2  = 32n^ + 4n taking all pointso rdered
C- exact only: 4n (4n+1)/2 taking exact points ordered
D- exact sym only: 4n (4n+1)/4 = 4n^2+n using sign symmetric

D is 2 times smaller yhan B but still quadratic

# Unum 2.0 Coolness

The fact that 1/x and -x are visible in the lattice circle, and this also applies to bounds of such numbers (Pbounds)

The following is an example of the 1/x values  the circle

<img src='doc/fractional.png' width=256/>

The following the inverse of a bound interval

<img src='doc/boundinverse.png' width=256/>

# Missing

- sqrt
- exp
- maximum
- computing storing the op tables
- full pbound operations

# Ideas

- cast map indices of Pnum given set A to indices of set B (e.g. from 16bit to 8bit and viceversa) assuming that the intervals are compatible (subset/superset)

