# Binomial Equation
 In [[S1 Binomial Theorem]], the binomial expansion given is the one below:

$\text{If }n>0$: 
$$(a+b)^n=
 \begin{pmatrix}n\\0\end{pmatrix}a^nb^0+
 \begin{pmatrix}n\\1\end{pmatrix}a^{n-1}b^1+
 \begin{pmatrix}n\\2\end{pmatrix}a^{n-2}b^2+
 \begin{pmatrix}n\\3\end{pmatrix}a^{n-3}b^3+ \cdots
 \begin{pmatrix}n\\n\end{pmatrix}a^0b^n$$
 $\text{Where}\begin{pmatrix}n\\r\end{pmatrix}=\mspace{0mu}^nC_r=\frac{n!}{r!(n-r)!}$
 $\mspace{0mu}$

This can be expanded to include any rational value of n, as shown below:

$\text{If }\lvert ax\rvert<1$:
$$(1+ax)^n\equiv1+
\frac{n}{1!}ax+
\frac{n(n-1)}{2!}(ax)^2+
\frac{n(n-1)(n-2)}{3!}(ax)^3+
\cdots$$

When n is not a positive whole number, it will become an infinite series as the numerator is never equal to 0.
As this is an approximation, it only works when $\lvert ax\rvert<1$. 

When $x$ is small, large powers of $x$ are extremely small, so they can be neglected. This means using the first few terms can approximate the original expression.

Note - "The expansion is valid" $\equiv$ "The result will converge" 
# Code
The code below will take the value of $a$ and $n$ in $(1+ax)^n$ and the term wanted, then calculate the coefficient of x of each term
```python
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
```