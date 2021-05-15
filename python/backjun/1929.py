import math
import sys


def solution(n):
    a = set([i for i in range(3, n+1, 2)])
    for i in range(3, n+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, n+1, i)])
    return len(a)+1


def solution2(n,m):
    a = set([i for i in range(n, m+1, 2)])
    for i in range(3, m+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, m+1, i)])
    return a

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True


def test(data):
    a = set(data)
    s = list(filter(is_prime_number, a))
    return len(s)


N,M = map(int, sys.stdin.readline().split(" "))
a= solution2(N, M)
for i in a:
    print(i)
