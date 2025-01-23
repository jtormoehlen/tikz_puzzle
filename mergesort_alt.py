
def mergesort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergesort(arr, left, mid)
        mergesort(arr, mid + 1, right)

        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:left+n1]
    R = arr[mid+1:mid+1+n2]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

data = [10, 7, 8, 9, 1, 5]
mergesort(data, 0, len(data) - 1)
print(data)

print()