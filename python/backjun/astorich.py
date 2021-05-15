import math
import sys
def solution(n): 
    a = set([i for i in range(3, n+1, 2)]) 
    for i in range(3, n+1, 2): 
        if i in a: 
            a -= set([i for i in range(i*2, n+1, i)]) 
    return len(a)+1


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


N= map(int, sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
print(test(arr))
