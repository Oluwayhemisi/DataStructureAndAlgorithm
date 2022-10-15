lst = [1, 2, 3, 4, 5, 6, 7]


def swap(lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst


print(swap(lst))
