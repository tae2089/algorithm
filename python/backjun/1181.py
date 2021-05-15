n = int(input())
#숫자를 입력받는다
array = []
for _ in range(n):
    num = input()
    array.append(num)

arr1 = sorted(set(array) , key= lambda x: (len(x),x))
for i in arr1:
    print(i)
