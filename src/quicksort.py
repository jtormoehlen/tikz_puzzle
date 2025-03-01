
def quicksort(arr, start, stop):
    if start < stop:
        pivot_index = partition(arr, start, stop)

        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, stop)

def partition(arr, start, stop):
    pivot = arr[stop]
    i = start - 1

    for j in range(start, stop):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[stop] = arr[stop], arr[i+1]
    return i + 1

data = [10, 7, 8, 9, 1, 5]
quicksort(data, 0, len(data) - 1)
print(data)