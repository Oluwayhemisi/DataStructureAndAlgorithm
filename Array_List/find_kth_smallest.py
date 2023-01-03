lst = [7, 10, 4, 3, 20, 15]
k = 3

mini_list = []


def kthsmallest(lst, k):
    minimum = lst[0]
    next_mini = lst[0]
    for i in range(len(lst)):
        if lst[i] < minimum:
            mini_list.append(lst[i])
    return mini_list

    # next_mini = minimum
    # minimum = lst[i]


print(kthsmallest(lst, k))
