#값을 입력받는다
# 테이블을 만들어준다.
N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))
# 반복문을 통해서 값을 만들어준다.
for i in range(1, N+1):
    for j in range(1,K+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value+knapsack[i-1][j-weight],knapsack[i-1][j])
