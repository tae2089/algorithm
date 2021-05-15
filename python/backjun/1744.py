from collections import deque
#0.결과값을 저장할 변수를 생성한다.
result = 0
#1. 몇개를 입력할지 받는다.
n = int(input())

#2. 값을 입력한다.
array = [int(input()) for _ in range(n)]

#3. 구분한 것을 오름차순으로 정렬해준다.
array.sort()
q = deque(array)

#4. 양수와 음수를 구분해준다.
positive = []
while q:
    num = q.pop()
    if num > 1:
        positive.append(num)
    else:
        q.append(num)
        break

# 0이하 수 저장
negative = []
while q:
    num = q.popleft()
    if num <= 0:
        negative.append(num)
    else:
        q.insert(0, num)
        break

#5. 2개씩 짝을 지워서 곱을 하고 결과값에 더해준다.
for i in range(0,len(positive),2):
    if i+1 < len(positive):
        result += positive[i] * positive[i+1]
    else:
        result += positive[i]

for i in range(0, len(negative), 2):
    if i+1 < len(negative):
        result += negative[i] * negative[i+1]
    else:
        result += negative[i]

#6. 나머지는 더해준다
while q:
    num = q.pop()
    result +=num