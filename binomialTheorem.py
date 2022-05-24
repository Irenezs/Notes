from fractions import Fraction
from math import factorial

def binomialCoeffCalculator(termNo: int, nVal: Fraction):
    numerator = 1
    for x in range(termNo):
        numerator *= (nVal - x)
    denominator = factorial(termNo)

    return Fraction(numerator,denominator)

def termCalculator(termNo: int,xVal,nVal: Fraction):
    return (xVal**termNo)*binomialCoeffCalculator(termNo,nVal)

xNum = int(input("Enter x coeff numerator : "))
xDen = int(input("Enter x coeff denominator : "))
x = Fraction(xNum,xDen)
nNum = int(input("Enter n numerator : "))
nDen = int(input("Enter n denominator : "))
n = Fraction(nNum,nDen)
terms = int(input("Enter terms wanted : "))
for term in range(terms):
    print(f"Term {term} : {termCalculator(term,x,n)}")