container = []


def rotate(lst):
    count = 0
    j = len(lst)-1
    for i in lst:
        sub = i[0]
        container.append(sub)
        count += 1
        if count == len(lst):
            print(container[::-1])


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(lst=lst))
