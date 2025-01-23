import random as rnd

def mergesort(numbers):
    mid = len(numbers) // 2

    if len(numbers) < 2:
        return numbers

    left = list(numbers[:mid])
    right = list(numbers[mid:])

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# data = [10, 7, 8, 9, 1, 5]
data = [rnd.randint(0, 1000) for _ in range(100)]
# data = []
print(data)
data = mergesort(data)
print(data)