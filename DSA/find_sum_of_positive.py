neg = []


def sum_integer(lst):
    pos = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            neg.append(lst[i])
        else:
            pos += lst[i]
    return pos


lst = [1, 2, 3, -3, 6, -8]

print(sum_integer(lst))
