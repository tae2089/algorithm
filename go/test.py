import sys
def f():
    h,m,s=map(int,input().split(":"))
    return 60*(60*h+m)+s

n,w=f(),f()
a = (n>=w)
print(a)
print(n,w)
M=w-n+86400*a
print(M)
print('%02d:%02d:%02d'%(M//3600,M%3600//60,M%3600%60))