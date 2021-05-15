import sys

N, S = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

start = 0
end = 1
result = N
sum = arr[start]
if sum == S:
    result = 1
flag = 0

while not (start == end == N):
    if sum < S and end < N:
        sum += arr[end]
        end += 1
    else:
        sum -= arr[start]
        start += 1

    if sum >= S:
        result = min(result, end-start)
        flag = 1

if flag == 0:
    print(0)
else:
    print(result)
