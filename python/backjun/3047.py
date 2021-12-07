# numbers = list(map(int,input().split()))
# order = list(input())
# order = list('ABC')
# order = 'ABC'
# def sort_number(t):
    # return t[0]
# print(sorted(zip([5,1,3],order),key=sort_number))

numbers = list(map(int,input().split()))
order = input()
numbers = sorted(numbers)

for i in order:
    if i == "A":
        print(numbers[0],end=' ')
    elif i == "B":
        print(numbers[1],end=' ')
    elif i == "C":
        print(numbers[2],end=' ')