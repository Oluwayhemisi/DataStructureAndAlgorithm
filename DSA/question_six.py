list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


# def foo(m):
#     v = m[0][0]
#     for row in m:
#         for element in row:
#             if v < element: v = element
#     return v
#
#
# print(foo(list[0]))


# def foo(value, lst):
#     value = 1
#     lst[0] = 44
#
#
# v = 3
# lst = [1, 2, 3]
# foo(v, lst)
# print(v, lst[0])


# def f(i, values = []):
#     values.append(i)
#     print(values),
#     return values
# f(1)
# f(2)
# f(3)

lst = [[1,2,3,4], [4,5,6,7], [8,9,10,11], [12, 13, 14, 15]]
for i in range(0,4):
    print(lst[i].pop())


