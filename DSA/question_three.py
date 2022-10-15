words = ['cat', 'mouse']
for word in words:
    print(len(word))


def func(x):
    return  x+ 1

f = func
print(f(2) + func(2))