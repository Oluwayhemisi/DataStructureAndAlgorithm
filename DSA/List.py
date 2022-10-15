list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

arr = list1 + list2
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)
