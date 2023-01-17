
def substring(s):
    cont = []
    count = 0
    for i in s:
        # if s.count(i) == 1:
        #     print(i)
        if i not in cont:
            cont.append(i)
            count += 1
    return count



s =  "pwwkew"
print(substring(s=s))
