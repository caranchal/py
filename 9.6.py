arr = [9,5,4,3,1,2]
arr[1:] = sorted(arr[1:])
print(arr)
arr = arr[:1] + sorted(arr[1:])
print(arr)