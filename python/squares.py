def square (x):
    x *= 2
    return x * x

n = 4

for i in range(7):
    print(n)
    if n:
        n -= 2
    else:
        n -= 1
        print(f'error {n}')
