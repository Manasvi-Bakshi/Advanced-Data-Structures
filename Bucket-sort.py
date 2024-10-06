def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    if not arr:  # Return if empty
        return arr
    
    n = len(arr)
    max_value = max(arr)
    
    # Create empty buckets
    buckets = [[] for _ in range(n)]
    
    # Distribute elements into buckets
    for num in arr:
        bi = int(n * num / (max_value if max_value > 0 else 1))  # Normalize
        buckets[min(bi, n - 1)].append(num)  # Ensure valid index

    # Sort buckets
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenate buckets into arr
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

# Get number of elements
num_elements = int(input("Enter number of elements: "))

# Initialize array
arr = []

# Get elements from user
for i in range(num_elements):
    element = float(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Sort the array
bucket_sort(arr)

# Output sorted array
print("Sorted array is:")
print(" ".join(map(str, arr)))
