# PythonBRMLtoolbox

## What is PythonBRMLtoolbox?
[BRMLtoolbox](http://web4.cs.ucl.ac.uk/staff/D.Barber/pmwiki/pmwiki.php?n=Brml.Software)
 in Python 3.7. My goal with this repository is to:
 1. Learn BRMLtoolbox with an insider perspective
 2. Provide a Python package for BRMLtoolbox which is available
    in MATLAB, Python 2.7 and Julia.
 3. Improve my Python skills
 
 ## Implementation details
 ### Variables
 When initializing a potential we can pass variables as arguments
 in different ways:
 * We can pass a scalar value (`int` or `float`) when we only
    have 1 variable. (We could also pass a list or a numpy array
    with only one value)
 
 ```python
import numpy as np
from brml.array import Array
pot = Array(variables=1)
pot2 = Array(variables=1.0)
pot3 = Array(variables=[1])
pot4 = Array(variables=np.array([1]))
pot5 = Array(variables=np.array([[1]]))
```
 * We can pass a `list` or a `numpy.array` when we have multiple variables.
 
```python
import numpy as np
from brml.array import Array
pot = Array(variables=[1, 2])
pot2 = Array(variables=np.array([1, 2]))
pot3 = Array(variables=np.array([[1, 2]]))
pot4 = Array(variables=np.array([[1], [2]]))
```
All of these calls are equivalent among them because they are all converted to 
a 1D `numpy.array` (notice that in MATLAB, because 1D arrays don't exist, this
is different).
It might be good to discuss whether it is better to convert all of these to 1D
`numpy.array` or to a 2D array with shape `(1, n)` where `n` is the number of
variables.

It is worth mentioning that you don't need to pass variables on initialization.
You can initialize an array without variables and without table, and add the later.
For example:
```python
import numpy as np
from brml.array import Array
pot = Array()
pot.set_variables(np.array([1, 2]))
```
Notice, however, that you CANNOT initialize variables before initializing the table.
That is, you cannot initialize an empty array `pot = Array()` and then call 
`pot.set_table(np.array([0.4, 0.6]))` because this will throw an error. You must
first use `set_variables` method, and after use the `set_table` method. If, instead, 
you decide to pass variables and table on initialization, then everything will be fine.

Go to `check/potential_variables.py` and you'll find a test to check
that the statements above are correct!

 ## What is BRMLtoolbox?
 The BRMLtoolbox is a MATLAB toolbox written by David Barber, Reader for the Computational Statistics and Machine Learning MSc at UCL. The BRML toolbox should be used together with the book Bayesian Reasoning and Machine Learning. It is a set of tools to help readers see how mathematical models translate into actual code.
 
 ## Software Requirements
 1. Python (3.6 onwards, although only type hints would need to be removed for Python 3.5)
 2. Numpy
 
 ## Mathematical Requirements
 The mathematical requirements for understanding classes within BRML toolbox are:
 1. Calculus & Linear Algebra
 2. Probability
 3. Algorithms
 4. Statistics (Bayesian mainly)
 I am currenlty trying to write an introduction to Probability here in [my Proofwiki account](https://proofwiki.org/wiki/User:MauroCamaraEscudero), although it is just a draft for now.
 
 ## Contributions
 Please feel free to contribute to this python version of the BRML toolbox! There are already a few incomplete implementations of the code, hopefully this version will be more up-to-date and efficient with your help!
 
 ## Reference & Book
 As I said earlier BRML toolbox comes with [Bayesian Reasoning and Machine Learning](http://web4.cs.ucl.ac.uk/staff/D.Barber/textbook/090310.pdf) book.
 
 ```
 @BOOK{barberBRML2012,
author = {Barber, D.},
title= {{Bayesian Reasoning and Machine Learning}},
publisher = {{Cambridge University Press}},
year = 2012}
```

 
 
