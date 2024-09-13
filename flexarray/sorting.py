#This file contains the sorting algorithms

#Bubble Sort
#This algorithm is suitable for small arrays.
#The time complexity of this algorithm is O(n^2).
#The space complexity of this algorithm is O(1).
#The algorithm is not suitable for large arrays.
def BubbleSort(arr):
    """Bubble Sort Algorithm. This function takes an array as input and returns the sorted array. Suitable for small arrays."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Selection Sort
#This algorithm is suitable for small arrays.
#The time complexity of this algorithm is O(n^2).
#The space complexity of this algorithm is O(1).
#The algorithm is not suitable for large arrays.
def SelectionSort(arr):
    """Selection Sort Algorithm. This function takes an array as input and returns the sorted array. Suitable for small arrays."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Insertion Sort
#This algorithm is suitable for small arrays.
#The time complexity of this algorithm is O(n^2).
#The space complexity of this algorithm is O(1).
#The algorithm is not suitable for large arrays.
def InsertionSort(arr):
    """Insertion Sort Algorithm. This function takes an array as input and returns the sorted array. Suitable for small arrays."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#Merge Sort
def MergeSort(arr):
    """Merge Sort Algorithm. This function takes an array as input and returns the sorted array. Suitable for large arrays."""
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)
        MergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

#Quick Sort
def QuickSort(arr):
    """Quick Sort Algorithm. This function takes an array as input and returns the sorted array. Suitable for large arrays."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)
    
#Heap Sort
def Heapify(arr, n, i):
    """Heapify function for Heap Sort."""
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr, n, largest)

def HeapSort(arr):
    """Heap Sort Algorithm. This function takes an array as input and returns the sorted array. Suitable for large arrays."""
    n = len(arr)
    for i in range(n//2, -1, -1):
        Heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)

#Counting Sort
#This algorithm shortens the time complexity of sorting by using a count array to store the count of each element.
#It is suitable for small arrays.
#The algorithm is not suitable for negative numbers.
#The algorithm is not suitable for floating point numbers.
#The algorithm is not suitable for large arrays.
def CountingSort(arr):
    """Counting Sort Algorithm. This function takes an array as input and returns the sorted array. Suitable for small arrays."""
    n = len(arr)
    output = [0]*n
    count = [0]*256
    for i in arr:
        count[ord(i)] += 1
    for i in range(1, 256):
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
    return

#Radix Sort
def CountingSortRadix(arr, exp):
    """Counting Sort for Radix Sort."""
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = arr[i]//exp
        count[index%10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        index = arr[i]//exp
        output[count[index%10]-1] = arr[i]
        count[index%10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
