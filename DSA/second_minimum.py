lst = [2, 4, 6, 10, 9, 5, 4, 10]
maximum = float('-inf')
second_max = float('-inf')

for i in lst:
    if i > maximum:
        second_max = maximum
        maximum = i
    elif i > second_max and i < maximum:
        second_max = i
print(second_max)



