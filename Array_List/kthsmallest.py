def kthSmallest(arr, n, k):
    lst = []
    get = arr.sort()
    print("get", get)
    print("get", arr)
    return arr[k-1]


array = [12, 3, 5, 7, 19]
n = len(array)
k = 2

print(kthSmallest(arr=array, n=n, k=2))
