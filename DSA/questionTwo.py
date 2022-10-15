# x = 51 % 3
# print(x)
lst = [1, 21, 3, 14, 5, 60, 7, 6]
k = 81
container = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == k:
            container.append(lst[i])
            container.append(lst[j])
print(container)
