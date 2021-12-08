from itertools import combinations

def check(values):
    total = sum(values)
    for i in range(2, total):
        if total % i == 0 : return False
    return True

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    for values in comb:
        if check(values) :answer += 1
    return answer