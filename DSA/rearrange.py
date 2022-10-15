lst = [10, -1, 20, 4, 5, -9, -6]

lst2 = []
lst3 = []


def arrange(lst):
    for i in lst:
        if i < 1:
            lst2.append(i)
        if i > 1:
            lst3.append(i)
    return lst2 + lst3


print(arrange(lst))



