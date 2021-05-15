N,M = map(int,input().split())
array = input().split()
array = list(map(lambda x: int(x), array))
# 투포인터 구현하기
test = 0
start = 0
end = 1
sum = array[start]
if sum == M:
    test += 1

while not (start == end == N):
    if sum < M and end < N:
        sum += array[end]
        end +=1
    else: 
        sum -= array[start]
        start+=1
        
    if sum == M:
        test +=1

print(test)
