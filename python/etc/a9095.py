#1,2,3 더하기 문제
a = [0, 1, 2, 4]
d = int(input())
c = 0
# A[i] = A[i-1] + A[i-2]  + A[i-3]
for j in range(4, d+1):
    c = a[j-1]+a[j-2]+a[j-3]
    a.append(c)
print(a[-1])
