lst = [1, 2, 3, 4, 5, 6, 7]
# [7,1,6,2,5,3,4]


new_list = []


def sorted_list(lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        new_list.append(lst[end])
        new_list.append(lst[start])
        start += 1
        end -= 1
    if len(new_list) % 2 == 0:
        new_list.pop()


    return new_list


print(sorted_list(lst))

# l =
