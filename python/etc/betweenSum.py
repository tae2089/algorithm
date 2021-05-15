def solution(a, b):
    answer = 0
    tmp = 0
    if a > b:
        tmp = a
        a = b
        b = tmp
    for i in range(a, b+1):
        answer += i
    return answer

def main():
    print(solution(3,5))

if __name__ == "__main__":
    main()