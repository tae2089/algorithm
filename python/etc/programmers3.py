def solution(progress, speed):
    # 배열을 생성한다. -> 횟수
    answer = []
    #반복문을 돌린다.
    while True:
        if  len(progress) ==0: 
            break
        if progress[0] >99:
            progress,a = popWork(progress,speed)
            answer.append(a)
        else:
            progress = getWork(progress,speed)
    return answer

def popWork(progress,speed):
    a = 0
    check_work = []
    for  v in progress:
        if  v > 99:
            check_work.append(v)
            a = a+1
        else:
            break
    for i in check_work:
        index = progress.index(i)
        progress.pop(index)
        speed.pop(index)
    return progress,a

def getWork(progress,speed):
    for i in range(len(progress)):
        progress[i] = progress[i] + speed[i]
    return progress

print(solution([93,30,55],[1,30,5]))
