from punum import *
import math

ap = Alphabet.p4();

print (dict(infinity=bin(ap.inf().v),one=bin(ap.one().v)))


#print (ap3.one())
a = Pbound.everything(ap)
print (a.v[0].v,a.v[1].v)

for i,x in enumerate(Pbound.everything(ap).iter()):
	ix = inv(x)
	nx = neg(x)
	#print (dict(index=i,valueindex=x.v,invindex=ix.v,negindex=nx.v,isstrictlynegative=x.isstrictlynegative(),isfractional=x.isfractional(),isinvfractional=ix.isfractional()))
	print ("\t",dict(index=i,value=str(x),inv=str(ix),beg=str(nx),abs=str(x.abs())))

# negatives are handled by flipping
print ("1.6",ap.convert(1.6)) # 1+
print ("---")
print ("2",ap.convert(2)) # exact
print ("0.1",ap.convert(0.2)) # MAYBE 0+ <<<<----- VERIFY
print ("0.4",ap.convert(0.4)) # MAYBE 0+ <<<<----- VERIFY
print ("0.5",ap.convert(0.5)) # exact
print ("2.5",ap.convert(2.5)) # 2+
print ("1.8",ap.convert(1.8)) # 1+
print ("1.2",ap.convert(1.2)) # 1+
print ("12000",ap.convert(1200)) # 2+
print ("inf",ap.convert(math.inf)) # inf