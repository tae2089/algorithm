from collections import deque

def solution(priorities, location):
    answer = 0
    a = deque((v,i) for i,v in enumerate(priorities))
    while a :
        value = a.popleft()
        if a and max(a)[0] > value[0]:
            a.append(value)
        else:
            answer +=1
            if value[1] == location:
                break
    return answer

def main():
    print(solution([1, 1, 9, 1, 1, 1], 0))

if __name__ =="__main__":
    main()


