lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]


def kadane(lst):
    globalmax = lst[0]
    currentmax = lst[0]
    for i in range(1, len(lst)):
        if currentmax < 0:
            currentmax = lst[i]
        else:
            currentmax += lst[i]
        if currentmax > globalmax:
            globalmax = currentmax
    return globalmax


print(kadane(lst))
