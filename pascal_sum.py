
def binom(i, j):
    if j == 0 or j == i:  # i == 0 or i == j
        return 1  # return 0
    else:
        return binom(i-1, j-1) + binom(i-1, j) 

def rec_sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + rec_sum(numbers[1:])

n = 7
total_sum = int()
for i in range(2, n):
    total_sum += rec_sum([binom(i, j) for j in range(1, i)])

print(total_sum)
# for i in range(n):
#     for j in range(i+1):
#         print(binom(i, j), end=' ')
#     print()