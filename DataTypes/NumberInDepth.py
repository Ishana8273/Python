print(0.1+0.1+0.4)

print(0.1+0.1+0.1-0.3)
# 5.551115123125783e-17
from decimal import Decimal

print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
# 0.0

from fractions import Fraction

myfrac = Fraction(1,3)
print(myfrac)

print(float(myfrac))