def fact(n):
    i = 0
    s = 1
    while i < n:
        if n in [0, 1]:
            return n
        s = s * (n - i)
        i = i + 1
    # return s
    print(s)

fact(4)
# print(fact(4))

# for i in range (0, 4):
#     print(i)

