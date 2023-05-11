def fact(n):
    if n <= 0:
        return 1
    return n * fact(n-1)

for i in range(21):
    print(i, '! =', fact(i))
