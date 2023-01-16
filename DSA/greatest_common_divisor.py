def greatest(num1, num2, ):
    gcd = 0
    lst = []
    min_value = min(num1, num2)
    max_value = max(num1, num2)
    if max_value % min_value == 0:
        gcd = min_value
        return gcd
    elif max_value % 2 != 0 and min_value % 2 != 0:
        return min_value
    else:
        for i in range(1, min_value + 1):
            if max_value % i == 0 and min_value % i == 0:
                lst.append(i)
                gcd = max(lst)
        return gcd


print(greatest(num1= 48, num2= 18))
