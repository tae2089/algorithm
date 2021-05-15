def solution(s):
    answer = True
    Queue = []
    for i in s:
        if i == '(':
            Queue.append('(')
        else:
            try:
                Queue.pop()
            except:
                return "NO"
    if len(Queue) == 0:
        return "YES"
    else:
        return "NO"

N = int(input().strip())
for i in range(N):
    text = input().strip()
    print(solution(text))