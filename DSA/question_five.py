lst = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    lst[i - 1] = lst[i]
for i in range(0, 6):
    print(lst[i])
