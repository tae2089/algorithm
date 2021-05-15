import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    N2 = int(sys.stdin.readline())
    if N2 != 0:
        arr.append(N2)
    else:
        arr.pop()
print(sum(arr))