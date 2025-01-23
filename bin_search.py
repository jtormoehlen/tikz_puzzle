
def binary_search(numbers, left, right, number):
    if right < left:
        return False
    
    mid = right + left // 2

    if numbers[mid] == number:
        return True

    else:
        if numbers[mid] < number:
            return binary_search(numbers, mid + 1, right, number)
        
        else:
            return binary_search(numbers, left, mid - 1, number) 
    
data = [10, 14, 17, 25, 33, 50, 51, 66, 100]
result = [binary_search(data, 0, len(data) - 1, i) for i in data]
result.extend(binary_search(data, 0, len(data) - 1, i) for i in [-3, 0, 101])
print([int(i == True) for i in result])