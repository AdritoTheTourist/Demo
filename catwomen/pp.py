def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in range(1, len(arr)):

        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


# Main program
arr = [5, 2, 8, 1, 3]

print("Original array:", arr)

arr = quick_sort(arr)

print("Sorted array:", arr)