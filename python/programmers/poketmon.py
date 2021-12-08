from itertools import combinations

def solution(nums):
    original_length = len(nums) // 2
    set_length = len(set(nums))
    if set_length < original_length:
        return set_length
    else:
        return original_length



