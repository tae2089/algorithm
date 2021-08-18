# 테스트 케이스 입력받기
t = int(input())

# dfs함수 구현하기


def dfs(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        if field[x][y] == 1:
            field[x][y] = 2
            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x-1, y)
            dfs(x+1, y)
            return 1
    return 0


for i in range(t):
    # 가로, 세로, 배추 개수 입력받기
    m, n, k = map(int, input().split())
    # 재배하는땅 리스트로 초기화하기
    field = [[0]*m for _ in range(n)]

# 배추 정보 입력받기
for i in range(k):
    a, b = map(int, input().split())
    field[b][a] = 1

# 지렁이 개수셀 변수 초기화하기
count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == 1:
            count += 1

print(count)
