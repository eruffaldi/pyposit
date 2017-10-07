from punum import *


ap3 = Alphabet.p3();

print (ap3.one())

for x in Pbound.everything(ap3).iter():
	print (x)