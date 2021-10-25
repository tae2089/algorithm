import sys

N = int(sys.stdin.readline())


def fatorial(N):
    if N <= 1:
        return 1
    else:
        return N * fatorial(N - 1)


print(fatorial(N))
