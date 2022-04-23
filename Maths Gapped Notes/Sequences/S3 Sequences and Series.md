# Sequences
Sequences can be described in two ways:
- Term-by-term : $u_{1}=x,\mspace{10mu}u_{n+1}=u_{n}+c$
- Position-to-term : $u_n=an+c$

There are a couple of other descriptors for sequences:
- An increasing sequence is one where :  $u_{n+1} > u_n$
- A decreasing sequence is one where :  $u_{n+1} < u_n$
- A periodic sequence is one where terms repeat : $u_{n+k} = u_n$ (So k is the period)

There is a key difference between a sequence and a series:

$x_n\mspace{1mu},x_{(n+1)}\mspace{1mu},x_{(n+2)}\mspace{1mu}x_{(n+3)}, \dots\mspace{10mu} \text{is a Sequence}$
$x_n+\mspace{1mu}x_{(n+1)}+\mspace{1mu}x_{(n+2)}+\mspace{1mu}x_{(n+3)}+ \dots\mspace{10mu} \text{is a Series}$

There are two types of Sequences in the spec:
- Arithmetic : $a,a+d,a+2d,a+3d,\cdots$
- Geometric : $a,ar,ar^2,ar^3,\cdots$

You can see that in arithmetic, a common difference d is added for the next term, and that in geometric, a common ratio r is multiplied for the next term, so we can see a term-by-term rule for both is:
- Arithmetic : $u_{n+1}=u_n+d$
- Geometric : $u_{n+1}=ru_n$

Both of these series have more useful position-to-term rules:
- Arithmetic : $u_n=a+(n-1)d$
- Geometric : $u_n=ar^n$
# Series
As can be inferred above, a series is the sum of each term in a sequence. Series and Sum are denoted by the letter $S$.
$$S_n\equiv u_1+u_2+\cdots+u_{n-1}+u_n \mspace{5em}\text{(True for every series)}$$
## Formulae
The summation of an arithmetic sequence is: $$S_n=\frac{n}{2}\Big[2a+(n-1)d\Big]$$
The summation of a geometric sequence is: $$S_n=\frac{a(1-r^n)}{(1-r)}$$
## Sum to Infinity
You may notice that in the sum of a geometric sequence, if $|r|<1$, $r^n$ will be approximately equal to 0, when n is very large. Thus, for a common ratio less than 1: $$S_\infty=\frac{a}{1-r}, \mspace{1em}\text{where |r|<1}$$
Because of this property, we can say a geometric sequence *diverges* when $|r|>1$, and *converges* when $|r|<1$.


## Sigma Notation
A common method of denoting series is using sigma notation:
$$\sum_{n=\varphi}^{k}{u_n}\equiv S_k-S_{\varphi-1}$$
- The bottom denotes what term of a series to start at
- The top denotes the last term of the sum
- The right denotes the series