n = int(input())
#숫자를 입력받는다
array = []
for _ in range(n):
    num = int(input())
    array.append(num)
array.sort()

for i in array:
    print(i)

