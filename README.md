# FlexArray

`FlexArray` is a Python library that provides an array-like structure with dynamic memory allocation features similar to C's `malloc`, `realloc`, and `free`.

## Installation

You can install the package via pip:

```bash
pip install flexarray
```

## Usage

```py
from flexarray.array import Array

# Create an array with initial size 3
arr = Array(3)
arr[0] = 10
arr[1] = 20
print(arr)  # Array([10, 20, None])

# Automatic dynamic resizing
arr[5] = 50
print(arr)  # Array([10, 20, None, None, None, 50])

# Malloc: Allocate memory dynamically
arr.malloc(5)
print(arr)  # Array([None, None, None, None, None])

# Realloc: Resize the array
arr.realloc(10)
print(arr)  # Array([None, None, None, None, None, None, None, None, None, None])

# Free: Deallocate memory
arr.free()
print(arr)  # Array([])

```