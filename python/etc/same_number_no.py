


def solution(arr):

    answer = []
    cnt = 0
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if answer[cnt] != arr[i]:
            answer.append(arr[i])
            cnt+=1
    return answer

def main():
    arr = [4, 4, 4, 3, 3]
    print(solution(arr))

if __name__ == "__main__":
    main()
