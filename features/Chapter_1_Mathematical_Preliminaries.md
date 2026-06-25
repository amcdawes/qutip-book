---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.4
kernel_info:
  name: python3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Chapter 1

An introduction to the Jupyter Notebook and some practice with probability ideas from Chapter 1.
## 1.1 Probability
### 1.1.1 Moments of Measured Data

The Jupyter Notebook has two primary types of cells "Markdown" cells for text (like this one) and "Code" cells for running python code. The cell below this one is a code cell that loads the plotting functions into the `plt` namespace and loads several functions from the `numpy` library. The last line requests that all plots show up inline in the notebook (instead of in other windows or as files on your computer).

```{code-cell} ipython3
import matplotlib.pyplot as plt
from numpy import array, sin, sqrt, dot, outer
%matplotlib inline
```

Arrays of data, and their average and sum in Python. We use some definitions from `numpy`. Notice the way these operators can be applied to arrays (with the "." operator).

```{code-cell} ipython3
x = array([1,2,3])
```

```{code-cell} ipython3
x.sum()
```

```{code-cell} ipython3
x.mean()
```

The formal definition (and to make sure we match with the book) is to take the sum and divide by the number of items in the sample:

```{code-cell} ipython3
x.sum()/len(x)
```

#### Higher order moments
Operate on the sample, python does this element-by-element, then do the same thing as above. You may be surprised that to raise a power is "**" instead of "^". This is a difference between python and other languages, just something to keep in mind!

```{code-cell} ipython3
x**2
```

```{code-cell} ipython3
(x**2).sum() # Note the parenthesis!
```

```{code-cell} ipython3
(x**2).sum()/len(x)
```

```{code-cell} ipython3
:inputHidden: false
:outputHidden: false

(x**2).mean()
```

### It works for functions too
`sin(x)` will find the `sin` of each element in the array `x`:

```{code-cell} ipython3
sin(x)
```

```{code-cell} ipython3
sin(x).sum()/len(x)
```

```{code-cell} ipython3
sin(x).mean()
```

#### Variance

```{code-cell} ipython3
x.var()  # Variance
```

```{code-cell} ipython3
x.std()  # Standard Deviation
```

We can test if two quanties are equal with the `==` operator. Not the same as `=` since the `=` is an assignment operator. This will trip you up if you are new to programming, but you'll get over it.

```{code-cell} ipython3
x.std()**2 == x.var()  # Related by a square root
```

### Example 1.1

```{code-cell} ipython3
x_m = array([9,5,25,23,10,22,8,8,21,20])
```

```{code-cell} ipython3
x_m.mean()
```

```{code-cell} ipython3
(x_m**2).sum()/len(x_m)
```

```{code-cell} ipython3
sqrt(281.3 - (15.1)**2)
```

```{code-cell} ipython3
x_m.std()
```

```{code-cell} ipython3
sqrt(281.3 - (15.1)**2) == x_m.std()
```

Close enough!



### 1.1.2 Probability



### Example 1.2
This is an illustration of how to implement the histogram from Example 1.2 in the text. Note the use of setting the number of bins. The `hist` command will pick for you, and you should try other values to see the impact. There is no one correct value, but the too many bins doesn't illustrate clusters of data, and too-few bins tends to oversimplify the data.

```{code-cell} ipython3
n, bins, patches = plt.hist(x_m,bins=7)
```

The hist function has several possible arguments, we use bins=7 to match the example.

```{code-cell} ipython3
# an array of the counts in each bin:
n
```

```{code-cell} ipython3
n/10.0*array([6,9,12,15,18,21,24])  # counts times each bin-center value
```

```{code-cell} ipython3
# sum of the last cell should be the mean:
sum(_)
```

```{code-cell} ipython3
n/10.0*array([6,9,12,15,18,21,24])**2  # counts times each bin-center value
```

```{code-cell} ipython3
# sum of the last cell should be the second moment:
sum(_)
```

Both of these results are close to the previous value, but not exact. Remember, the historgram is a representation of the data and the agreement will improve for larger data sets.



## 1.2 Linear Algebra
### 1.2.1 Vectors and Basis sets
We'll use the qutip library later, even though this is all just linear algebra. For now, try using standard-python for vector math:

```{code-cell} ipython3
rvec = array([1,2])  # A row vector
```

```{code-cell} ipython3
rvec
```

```{code-cell} ipython3
cvec = array([[1],[2]])  # A column vector
```

```{code-cell} ipython3
cvec
```

```{code-cell} ipython3
cvec*rvec # Actually the outer product:
```

```{code-cell} ipython3
:inputHidden: false
:outputHidden: false

rvec*cvec # still the outer product... so this simple `*` doesn't respect the rules of linear algebra!
```

The `dot` function properly computes the dot product that we know and love from workshop physics:

```{code-cell} ipython3
dot(rvec,cvec)
```

```{code-cell} ipython3
outer(cvec,rvec)
```

```{code-cell} ipython3
# This doesn't work if you try to run it because `dot` knows what shape the vectors should be

# dot(cvec,rvec)  
```

This probably isn't your first error message, but it's important to look at what Python is telling you. First, it lists the type of error (ValueError). Then it shows where the error occured (in the dot function). This is helpful when you have larger cells with more lines in them. Obviously we already know what line caused this error since there is only one. Finally, the error is explained as follows: the shapes are not aligned, meaning the vectors don't have the right dimensions for a dot product. Some error messages are more helpful than others, but they all look like this. An error and a traceback.
