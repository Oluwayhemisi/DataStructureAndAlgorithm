# lst = [9, 2, 3, 2, 6, 6]
lst = [4, 5, 1, 2, 0, 4]
p = 0


def find_first_unique(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] != lst[j]:
                return lst[i]
    return


print(find_first_unique(lst))


# customers = ['Marie', 'Anne', 'Donald']
# customers[2:4] = ['Barack', 'Olivia', 'Sophia']
# print(customers)
