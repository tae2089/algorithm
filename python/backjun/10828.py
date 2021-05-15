import sys
N = sys.stdin.readline()
arr = []
for i in range(int(N)):
    S = sys.stdin.readline()
    S = S.split()
    if S[0] == "push":
        arr.append(S[1])
    elif S[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            a = arr.pop()
            print(a)
    elif S[0] == "size":
        print(len(arr))
    elif S[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif S[0] == "top":
        if len(arr) == 0:
                print(-1)
        else:
            print(arr[-1])
    



