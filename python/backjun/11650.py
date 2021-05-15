n = int(input())
#숫자를 입력받는다
array = []
for _ in range(n):
    num1,num2 = map(int, input().split())
    array.append((num1,num2))

arr1=sorted(array, key=lambda x: (x[0], x[1]))
for i in arr1:
    print(i[0],i[1])
