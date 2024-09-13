def SumOfElements(arr):
    """Returns the sum of all elements in the array."""
    total = 0
    for element in arr:
        total += element
    return total

def AverageOfElements(arr):
    """Returns the average of all elements in the array."""
    total = SumOfElements(arr)
    return total / len(arr) if len(arr) > 0 else 0

def MaxElement(arr):
    """Returns the maximum element in the array."""
    if len(arr) == 0:
        return None
    max_elem = arr[0]
    for element in arr:
        if element > max_elem:
            max_elem = element
    return max_elem

def MinElement(arr):
    """Returns the minimum element in the array."""
    if len(arr) == 0:
        return None
    min_elem = arr[0]
    for element in arr:
        if element < min_elem:
            min_elem = element
    return min_elem

def ProductOfElements(arr):
    """Returns the product of all elements in the array."""
    if len(arr) == 0:
        return 1
    product = 1
    for element in arr:
        product *= element
    return product

def CountOccurrences(arr, target):
    """Counts the number of occurrences of the target element in the array."""
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count

def CountAllOccurrences(arr):
    """Returns array for all elements and their occurrences in the array."""
    freq = {}
    for element in arr:
        freq[element] = freq.get(element, 0) + 1
    return freq

def ReverseArray(arr):
    """Returns the array in reverse order."""
    return arr[::-1]

def IsSorted(arr):
    """Checks if the array is sorted in non-decreasing order."""
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def MedianOfElements(arr):
    """Returns the median of the array. The array must be sorted."""
    if len(arr) == 0:
        return None
    arr = sorted(arr)
    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]

def ModeOfElements(arr):
    """Returns the mode (most frequent element) of the array."""
    if len(arr) == 0:
        return None
    freq = {}
    for element in arr:
        freq[element] = freq.get(element, 0) + 1
    mode = max(freq, key=freq.get)
    return mode

def Variance(arr):
    """Returns the variance of the array."""
    if len(arr) == 0:
        return 0
    avg = AverageOfElements(arr)
    variance = sum((x - avg) ** 2 for x in arr) / len(arr)
    return variance

def StandardDeviation(arr):
    """Returns the standard deviation of the array."""
    return Variance(arr) ** 0.5
