def min_max(lst):
    mini = lst[0]
    maxi = lst[0]
    for i in range(len(lst)):
        if len(lst) == 1:
            return
        if lst[i] < mini:
    
            print(f'{lst[i]}, "<", {mini}')
            mini = lst[i]
        if lst[i] > maxi:
            maxi = lst[i]

    print("the minimum is:", mini, "the maximum is:", maxi)


lst = [22, 14, 8, 17, 35, 3]
print(min_max(lst))
