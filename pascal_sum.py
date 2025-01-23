
def binom(i, j):
    if j == 0 or j == i:
        return 1
    else:
        return binom(i-1, j-1) + binom(i-1, j)

def sum_rec(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_rec(numbers[1:])

n = 7
inner_sum = int()
for i in range(2, n):
    inner_sum += sum_rec([binom(i, j) for j in range(1, i)])

print(inner_sum)
# for i in range(n):
#     for j in range(i+1):
#         print(binom(i, j), end=' ')
#     print()