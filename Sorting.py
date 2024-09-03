def printArray(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

def Insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def Selection(arr):
    for i in range(len(arr)):
        min = i

def Bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def main():
    if __name__ == "__main__":
        default = []
        arr = [12, 11, 13, 5, 6]
        arr = default
        print("The input array that needs to be sorted is: ")
        printArray(arr)
        print("The Sorted Array is: \n")
        printArray(arr)
        arr = default
