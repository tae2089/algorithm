def solution(s):
    answer = 0
    s_plus = s.count('-')
    if s_plus == 1:
        sn = s[1:]
        answer = int(sn) * -1
    else:
        answer = int(s)
    return answer

def main():
    print(solution("1234"))

if __name__ == "__main__":
    main()