def print_array(arr):
    """Print array elements."""
    print(" ".join(map(str, arr)))

def insertion_sort(arr):
    """Insertion Sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    """Selection Sort."""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    """Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge(arr, left, mid, right):
    """Merge two halves."""
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        arr[k] = L[i] if L[i] <= R[j] else R[j]
        if L[i] <= R[j]:
            i += 1
        else:
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

def merge_sort(arr, left, right):
    """Merge Sort."""
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def partition(arr, low, high):
    """Partition for Quick Sort."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """Quick Sort."""
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    """Demonstrate sorting algorithms."""
    arr = [12, 11, 13, 5, 6]
    print("Input array:")
    print_array(arr)

    insertion_sort(arr.copy())
    print("Insertion Sort:")
    print_array(arr)

    selection_sort(arr.copy())
    print("Selection Sort:")
    print_array(arr)

    bubble_sort(arr.copy())
    print("Bubble Sort:")
    print_array(arr)

    arr_copy = arr.copy()
    merge_sort(arr_copy, 0, len(arr_copy) - 1)
    print("Merge Sort:")
    print_array(arr_copy)

    arr_copy = arr.copy()
    quick_sort(arr_copy, 0, len(arr_copy) - 1)
    print("Quick Sort:")
    print_array(arr_copy)

if __name__ == "__main__":
    main()
