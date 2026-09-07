def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Input
arr = list(map(int, input("Enter the array elements: ").split()))
key = int(input("Enter the element to search: "))

# Function Call
result = linear_search(arr, key)

# Output
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")