# from Slide 21 "Divide by 0" slide 
# The SORN has 10 presence bits set to represent the half-open interval (–1, 2].  Begin by taking the reciprocal, which is lossless and preserves the contiguity of the unums in the result.
from punum import *

a = Alphabet.p2()

x  = Pbound((-a.one()).next(),a.one().next().next())
print (x)
print (~x)