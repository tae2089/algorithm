def solution2(n, m):
    a = set([i for i in range(n, m+1, 2)])
    for i in range(n, m+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, m+1, i)])
    return a


N, M = map(int, input().split())
a = solution2(N, M)
for i in a:
    print(i)
