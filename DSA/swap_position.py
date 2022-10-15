def swap(lst):
    start = 0
    end = len(lst) - 1
    for i in range(len(lst)):
        start = 0

        end = len(lst) - 1
        lst[start], lst[end] = lst[end], lst[start]
        return lst