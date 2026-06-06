"""NumPy: fast array operations, vectorized math, and broadcasting -
the foundation almost every data/ML library in Python builds on."""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr, arr.dtype, arr.shape)

# Vectorized operations - applied to every element at once, no Python loop
print(arr * 2)
print(arr ** 2)
print(arr + np.array([10, 20, 30, 40, 50]))

# Broadcasting: operations between arrays of different (compatible) shapes
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix + 100)              # scalar broadcast to every element
print(matrix + np.array([1, 0, -1]))   # row broadcast across every row

# Aggregations
print("sum:", arr.sum(), "mean:", arr.mean(), "std:", arr.std())
print("column sums:", matrix.sum(axis=0))
print("row sums:", matrix.sum(axis=1))

# Indexing and boolean masking
print(arr[1:4])
mask = arr > 2
print(mask)
print(arr[mask])   # only elements where the mask is True

# Useful constructors
print(np.zeros((2, 3)))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
