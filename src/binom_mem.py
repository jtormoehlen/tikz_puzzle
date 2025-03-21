def binom(i, j, memo={}):  # def binom(i, j, memo=()) #distractor
    if (i, j) in memo:  # if {i, j} in memo: #distractor
        return memo[i, j]
    if j == 0 or j == i:
        return 1
    else:
        memo[i, j] = binom(i - 1, j, memo) + binom(i - 1, j - 1, memo)  # memo[i, j] = binom(i, j - 1, memo) + binom(i - 1, j - 1, memo)
        return memo[i, j]

# def binom(i, j):
#     if j == 0 or j == i:
#         return 1
#     else:
#         return binom(i - 1, j) + binom(i - 1, j - 1)

print(binom(768, 572))