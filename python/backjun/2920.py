import sys

arr = list(map(int, sys.stdin.readline().split(" ")))

arr2 = sorted(arr)
arr3 = sorted(arr,reverse=True)
print(arr2 == arr)