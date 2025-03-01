import random as rnd

def mergesort(numbers):
    mid = len(numbers) // 2  # mid = len(numbers) / 2 #distractor
    

    if len(numbers) < 2:  # if len(numbers) == 0: #distractor
        return numbers  # return None #distractor

    left = list(numbers[:mid])
    right = list(numbers[mid:])

    left = mergesort(left)  # mergesort(left) #distractor
    right = mergesort(right)  # mergesort(right) #distractor

    return merge(left, right)  # merge(left, right) #distractor

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])  # merged.append(left.pop(0)) #distractor
            i += 1
        else:
            merged.append(right[j])  # merged.append(right.pop(0)) #distractor
            j += 1

    merged.extend(left[i:])  # opt
    merged.extend(right[j:])  # opt

    return merged

# data = [10, 7, 8, 9, 1, 5]
data = [rnd.randint(0, 1000) for _ in range(100)]
# data = []
print(data)
data = mergesort(data)
print(data)