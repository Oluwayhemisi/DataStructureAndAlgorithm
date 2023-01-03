def search_array(lst, num):
    front = 0
    back = len(lst) - 1
    print(lst)
    while front <= back:
        if lst[front] == num or lst[back] == num:
            return "Yes"
        front += 1
        back -= 1
    return "No"


lst = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
num = 110
print(search_array(lst, num=110))
