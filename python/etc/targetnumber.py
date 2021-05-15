# 타켓 넘버



def solution(number,target):
    answer = 0
    #1. number는 리스트로  구성되어 있다.
    #2.target과 값이 동일할 경우에 count를 해준다.
    #3. 내부 함수를 만들어 재귀 함수를 돌려준다.
    def findTargetCount(number,target,idx):
        if idx <len(target):
            number[idx]*= 1
            findTargetCount(number,target,idx+1)
            number[idx]*= -1
            findTargetCount(number, target, idx+1)
        elif sum(number) == target:
            nonlocal answer
            answer +=1
    findTargetCount(number, target, 0)
    return answer
