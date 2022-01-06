---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Chapter 10: Position and Momentum
We can start using sympy to handle symbolic math (integrals and other calculus):

```{code-cell} ipython3
from sympy import *
```

```{code-cell} ipython3
init_printing(use_unicode=True)
```

```{code-cell} ipython3
x, y, z = symbols('x y z', real=True)
a, c = symbols('a c', nonzero=True, real=True)
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

The cell below will return an odd set of conditions on the result. This is because the solver doesn't want to assume anything about `a` and there is a special case where the answer would be different. If you look closely though, that special case isn't physically realistic so to igore these special conditions, we add `conds='none'`. The next cell down does what you'd expect. From here on out, just add this to the `integrate` function and we'll get what we expect.

```{code-cell} ipython3
A = (c*cos((pi*x)/(2.0*a)))**2
A.integrate((x,-a,a))
```

```{code-cell} ipython3
A = (c*cos((pi*x)/(2.0*a)))**2
A.integrate((x,-a,a), conds='none')
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
```

```{code-cell} ipython3
E.n()  # the .n() method approximates the numerical part. You can look at the full expression below.
```

```{code-cell} ipython3
E
```

## Example 10.2

```{code-cell} ipython3
h = Symbol('hbar', real=True)
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
```

This is as far as we can go in sympy. Unfortunately, any other momentum integrals choke. Off to sage math and the maxima algebra engine that runs it.

```{code-cell} ipython3

```
