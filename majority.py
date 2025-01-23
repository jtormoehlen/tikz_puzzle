import random as rand

def count_elem(arr, elem, left, right):
    count = 0
    for i in range(left, right + 1):
        if arr[i] == elem:
            count += 1
    return count

def maj_elem(arr, left, right):

    if left == right:
        return arr[left]

    mid = (left + right) // 2
    maj_left = maj_elem(arr, left, mid)
    maj_right = maj_elem(arr, mid + 1, right)

    print(arr[left:mid])
    print(arr[mid+1:right])
    print(f'left: {maj_left} | right: {maj_right}')

    if maj_left == maj_right:
        return maj_left

    count_left = sum(1 for i in range(left, right + 1) if arr[i] == maj_left)
    count_right = sum(1 for i in range(left, right + 1) if arr[i] == maj_right)
    # count_left = count_elem(arr, maj_left, left, right)
    # count_right = count_elem(arr, maj_right, left, right)

    if count_left > (right - left + 1) // 2:
        return maj_left
    elif count_right > (right - left + 1) // 2:
        return maj_right
    else:
        return None

    # Example usage 
# arr = [2, 2, 1, 1, 1, 2, 2] 
# arr = [6, 7, 6, 6, 6, 3, 2, 6, 6, 1, 6]
arr = [i for i in range(10)]
majority = maj_elem(arr, 0, len(arr) - 1) 
print("Majority Element:", majority) 
