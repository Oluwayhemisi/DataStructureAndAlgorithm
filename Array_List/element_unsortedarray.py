# Given an array of n distinct integers and an element x. Search the element x in the array using minimum
# number of comparisons. Any sort of comparison will contribute 1 to the count of comparisons. For
# example, the condition used to terminate a loop, will also contribute 1 to the count of comparisons each
# time it gets executed. Expressions like while (n) {n–;} also contribute to the count of comparisons as
# value of n is being compared internally so as to decide whether or not to terminate the loop


def func(lst, num):
    for i in range(0, len(lst)):
        if lst[i] == num:
            print(lst[i])
            return "found"
    return "not found"


# listt = [4, 6, 1, 5, 8]
listt = [10,3,12, 7, 2, 11, 9]
x = 1

print(func(lst=listt, num=x))
