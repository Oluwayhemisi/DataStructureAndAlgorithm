def findMinimum(lst):
    mini = lst[0]
    for i in range(len(lst)):
        if lst[i] < mini:
            mini = lst[i]
    print(mini)


list = [9, 2, 3, 6]
print(findMinimum(list))
