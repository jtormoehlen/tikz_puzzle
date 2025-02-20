
def binom(i, j):
    if j == 0 or j == i:  # i == 0 or i == j #distractor
        return 1  # return 0 #distractor
    else:  # opt
        return binom(i-1, j-1) + binom(i-1, j)  # return binom(i, j-1) + binom(i-1, j-1) #distractor

def rec_sum(numbers):
    if not numbers:  # if not numbers: #distractor
        return 0
    else:  # opt
        # numbers = numbers[1:-1] #distractor
        return numbers[0] + rec_sum(numbers[1:])  #  return numbers[0] + numbers[-1] + sum_rec(numbers[1:-1]) #distractor

n = 7
total_sum = int()
for i in range(2, n):  # for j in range(2, n): #distractor
    total_sum += rec_sum([binom(i, j) for j in range(1, i)])  # total_sum += sum_rec([binom(i, j) for i in range(1, j)]) #distractor

print(total_sum)
# for i in range(n):
#     for j in range(i+1):
#         print(binom(i, j), end=' ')
#     print()