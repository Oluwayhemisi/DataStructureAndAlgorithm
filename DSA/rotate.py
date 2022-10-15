lst = [10, 20, 30, 40, 50]
k = 2

lst2 = []


# def rotate(lst, k):
#     if k > 0:
#         return
#     else:
#         for i in lst:
#             for j in k:
#                 get = len(lst - i)
#                 lst2.append(get) + lst[0:2]
#     print(lst2)


def rotates(lst, k):
        return lst[-k: ] + lst[:len(lst)-k]


print(rotates(lst, 2))


# def get(lst):
#     return lst[-2:]
# print(get(lst))