a, b = 0, 1
while b < 5:
    print(b)
    a, b = b, a + b
    print(f'{a}, {b} "=" {b}, {a + b}')
