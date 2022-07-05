def solution(s):
    stack = []
    for value in s:
        if stack:
            if stack[-1] == value:
                stack.pop()
            else:
                stack.append(value)
        else:
            stack.append(value)
    if len(stack) == 0: return 1
    else: return 0

a = solution(['a','a'])
print(a)