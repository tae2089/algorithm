
def solution2(n, lost, reserve):
    answer=0
    com = set(lost).intersection(reserve)
    for i in com:
        reserve.pop(reserve.index(i))
        lost.pop(lost.index(i))
    answer = n - len(lost)
    
    for i,v in enumerate(lost):
        if v+1 in reserve:
            reserve.pop(reserve.index(v+1))
            answer = answer + 1
        elif v-1 in reserve:
            reserve.pop(reserve.index(v-1))
            answer = answer + 1
    return answer

def solution(a, b):
    month = 'FRI,SAT,SUN,MON,TUE,WED,THU'.split(",")
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = month[(sum(days[:a-1])+b-1) % 7]
    return answer


def solution3(number,k):
    answer = ''
    n = len(number)-k
    number = list(number)
    dp = list()
    for i in range(n):
        max_num = 0
        c = ''
        for num in number:
            if i == 0:
                if max_num < int(num):
                    max_num = int(num)
                    c = num
            else:
                if max_num < int(dp[i-1]+num):
                        max_num = int(dp[i-1]+num)
                        print(max_num)
                        c = num
        dp.append(str(max_num))
        number.pop(number.index(c))
    return dp[-1]


print(solution3("4177252841", 4))
