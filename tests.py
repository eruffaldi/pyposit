from punum import *


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

print ("1.6",ap.convert(1.6))
print ("---")
print ("2",ap.convert(2))
print ("0.5",ap.convert(0.5))
print ("2.5",ap.convert(2.5))
print ("1.8",ap.convert(1.8))
print ("1.2",ap.convert(1.2))