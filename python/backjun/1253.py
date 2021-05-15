n = int(input())
array = input().split()
array = list(map(lambda x: int(x), array))
array.sort()
#숫자를 입력받는다
arr2 = []

for i in range(len(array)):
    

    for j in range(i+1,len(array)):
        num = array[i]+array[j]
        if num in array:
            if num not in arr2:
                arr2.append(num)
print("good:",len(arr2))
