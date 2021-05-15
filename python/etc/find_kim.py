def solution(seoul):
    answer = ''
    if len(seoul) > 1 & len(seoul) < 1000:
        answer = "김서방은 {}에 있다".format(seoul.index("Kim"))
    return answer
def main():
    seoul = ['s','Kim']
    print(solution(seoul))

if __name__ == "__main__":
    main()