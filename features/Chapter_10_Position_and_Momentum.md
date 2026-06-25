---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.4
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Chapter 10 - Position and Momentum
We can start using sympy to handle symbolic math (integrals and other calculus):

```{code-cell} ipython3
from sympy import *
```

```{code-cell} ipython3
init_printing(use_unicode=True)
```

```{code-cell} ipython3
# SymPy works better if you specify what letters are symbols:
x, y, z = symbols('x y z', real=True)

# notice we can also put some restrictions on the symbols:
a, c = symbols('a c', nonzero=True, real=True) 
```

```{code-cell} ipython3
integrate?
```

There are two ways to use the `integrate` function. In one line, like `integrate(x,(x,0,1))` or by naming an expression and then integrating it over a range:

```
A = (c*cos((pi*x)/(2.0*a)))**2
A.integrate((x,-a,a),conds='none')
```

We'll use both, at different times. For longer expressions, the second form can be easier to read and write.

First, just try the following, then we'll re-create some examples in the book.

```{code-cell} ipython3
integrate(x,(x,0,1))
```

```{code-cell} ipython3
integrate(x**2,(x,0,1))
```

```{code-cell} ipython3
A = (c*cos((pi*x)/(2.0*a)))**2
A.integrate((x,-a,a))
```

So this tells us the normalization constant should be $c=\frac{1}{\sqrt{a}}$. Check that it is normalized if we do that:

```{code-cell} ipython3
psi = 1/sqrt(a)*cos((pi*x)/(2.0*a))  # notice we can name the expression something useful.
B = psi**2
B.integrate( (x,-a,a), conds='none')
```

Because `psi` is a real function, we can calculate expectation values by integrating over $x$ or $x^2$ with `psi**2`:

```{code-cell} ipython3
C = x*psi**2
C.integrate( (x,-a,a), conds='none')
```

```{code-cell} ipython3
D = x**2 * psi**2
E = D.integrate( (x,-a,a), conds='none')
E
```

```{code-cell} ipython3
E.simplify()  # this is a useful method!
```

```{code-cell} ipython3
E.n()  # the .n() method approximates the numerical part. You can look at the full expression below.
```

## Example 10.2

```{code-cell} ipython3
h = Symbol('hbar', real=True, positive=True)
```

Use the `diff` function to take a derivative of a symbolic expression. For example:

```{code-cell} ipython3
diff(x**2, x)
```

```{code-cell} ipython3
# Solution
-1j*h*diff( 1/a*cos((pi*x)/(2*a)) ,x)
```

```{code-cell} ipython3
# Solution
B1 = (pi*h/(2*a))**2 * (cos((pi*x)/(2*a)))**2
B1.integrate( (x,-a,a), conds='none' )
```

## Example 10.3

```{code-cell} ipython3
p = Symbol('p', real=True) 
```

```{code-cell} ipython3
# Solution
A = integrate(1/sqrt(2*pi*a*h)*exp(-I*p*x/h)*cos((pi*x)/(2*a)),(x,-a,a), conds='none')
```

```{code-cell} ipython3
# Solution
A
```

```{code-cell} ipython3
psi_p = sqrt(2*a*pi/h) * 2/(pi**2 - (2*p*a/h)**2) * cos(p*a/h)
psi_p
```

```{code-cell} ipython3
psi_p == sqrt(2*a*pi/h)*2/(pi**2 - (2*p*a/h)**2) * cos(p*a/h)
```

Which agrees with the book.

This is about as far as we can go in sympy. Unfortunately, many other momentum integrals choke. There are a few hints to get through the rest here:



## Problem 10.3

```{code-cell} ipython3
x, y, z = symbols('x y z', real=True)
a, c = symbols('a c', nonzero=True, real=True, positive=True)

psi = c*1/(a**2 + x**2)  # define the wavefunction with c constant
int1 = integrate(psi*psi,(x,-oo,oo), conds='none')  # integrate psi^2
solutions = solve(int1 - 1,c)  # solve for c, this returns a list of solutions
c2 = simplify(solutions[0])  # simplify the solution for c:
c2
```

```{code-cell} ipython3
psi2 = c2/c*psi
psi2
```

```{code-cell} ipython3
integrate(psi2 * x * psi2,(x,-oo,oo))
```

```{code-cell} ipython3
integrate(psi2 * x**2 * psi2,(x,-oo,oo))
```

So $\Delta x^2 = a^2 - 0^2$ therefore $\Delta x = a$



## Problem 10.17:
Now find the momentum representation of the state from 10.3

```{code-cell} ipython3
p = symbols('p', nonzero=True, real=True, positive=True)
B = integrate(sqrt(1/(2*pi*h))*exp(-I*p*x/h)*psi2,(x,-oo,oo))
B
```

```{code-cell} ipython3
B.simplify()
```

This agrees with the book after we notice that we had to force $p$ to be positive in order to get the integral to converge. The book has $|p|$ in the argument of the exponent to reflect this constraint.



## Problem 10.13

```{code-cell} ipython3
psi = 1/sqrt(2*a)*sech(x/a)
dpsi = diff(psi,x)
dpsi
```

```{code-cell} ipython3
ddpsi = diff(dpsi,x)
ddpsi = ddpsi.simplify()
ddpsi
```

```{code-cell} ipython3
expect_p = integrate(psi*ddpsi,(x,-oo,oo))
expect_p
```

```{code-cell} ipython3

```
