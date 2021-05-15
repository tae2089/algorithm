def solution(s):
    a = len(s)//2
    if (len(s) % 2) == 0:
        answer = s[a-1:a+1]
    else:
        answer = s[a]
    return answer

print(solution('abcd'))
