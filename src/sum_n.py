def sum_odd(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total


S = lambda n : (n + 1) ** 2 / 4

# Beispielaufruf
n = 21

print(sum_odd(n))
print(S(n))


def gauss_odd(n):
    if n == 1:
        return 1
    else:
        return n + gauss_odd(n - 2)
    
print(gauss_odd(n))