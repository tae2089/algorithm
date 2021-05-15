import sys
S = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())
point = len(S)
for _ in range(N):
    V = sys.stdin.readline().strip()
    V = V.split()
    if V[0] == "P":
        S.insert(point, V[1])
        point = point + 1
    elif V[0] == "L":
        if point <= 0:
            point = 0
        else:
            point = point-1
    elif V[0] == "D":
        if point >= len(S):
            point = len(S)
        else:
            point = point+1
    elif V[0] == "B":
        if point != 0:
            del S[point-1]
            point = point-1
print("".join(S))
