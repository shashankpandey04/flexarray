
def LinearSearch(arr, target):
    """Linear Search Algorithm. This function takes an array and a target value as input and returns the index of the target value in the array."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def BinarySearch(arr, target):
    """Binary Search Algorithm. This function takes a sorted array and a target value as input and returns the index of the target value in the array."""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def JumpSearch(arr, target):
    """Jump Search Algorithm. This function takes a sorted array and a target value as input and returns the index of the target value in the array."""
    n = len(arr)
    step = int(n**0.5)
    prev = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

def InterpolationSearch(arr, target):
    """Interpolation Search Algorithm. This function takes a sorted array and a target value as input and returns the index of the target value in the array."""
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def ExponentialSearch(arr, target):
    """Exponential Search Algorithm. This function takes a sorted array and a target value as input and returns the index of the target value in the array."""
    n = len(arr)
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return BinarySearch(arr[:min(i, n)], target)

def TernarySearch(arr, target):
    """Ternary Search Algorithm. This function takes a sorted array and a target value as input and returns the index of the target value in the array."""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1

def FibonacciSearch(arr, target):
    """Fibonacci Search Algorithm. This function takes a sorted array and a target value as input and returns the index of the target value in the array."""
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n-1)
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and arr[offset+1] == target:
        return offset+1
    return -1