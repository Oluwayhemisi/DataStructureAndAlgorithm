lst = []


def decimal(num):
    if num > 0:

        decimal(num//2)
        print(f'{num} "num" "//" {2} ')
        print(num % 2)

    # get_quotient = num // 2
    # get_remainder = num % 2
    # if get_quotient == 0:
    #     return get_remainder
    # else:
    #     decimal((num) // 2)
    #     # print(f'{num} "num" "//" {2} ')
    # print(num % 2)



num = 10
print(decimal(10))
