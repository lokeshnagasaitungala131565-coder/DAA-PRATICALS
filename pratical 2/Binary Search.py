def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input
arr = list(map(int, input("Enter the sorted array elements: ").split()))
key = int(input("Enter the element to search: "))

# Function Call
result = binary_search(arr, key)

# Output
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")