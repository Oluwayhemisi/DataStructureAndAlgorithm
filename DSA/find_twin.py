

def get_twin(lst):
    for i in range(0, len(lst) - 1, 2):
        if lst[i] != lst[i + 1]:
            return lst[i]
        elif lst[-1] != lst[-2]:
            return lst[-1]
    return -1




list = [1, 1, 2, 2, 4]
print(get_twin(list))
