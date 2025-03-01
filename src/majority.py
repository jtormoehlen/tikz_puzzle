
def maj_elem(numbers, left, right):

    if left == right:  # if left >= right: #distractor
        return numbers[left]  # return None #distractor

    mid = (left + right) // 2
    maj_left = maj_elem(numbers, left, mid)  # maj_elem(numbers, left, mid) #distractor
    maj_right = maj_elem(numbers, mid + 1, right)  # maj_elem(numbers, mid + 1, right) #distractor

    if maj_left == maj_right:  # if maj_left != maj_right: #distractor
        return maj_left  # return None #distractor

    count_left = sum(1 for i in range(left, right + 1) if numbers[i] == maj_left)
    count_right = sum(1 for i in range(left, right + 1) if numbers[i] == maj_right)

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
