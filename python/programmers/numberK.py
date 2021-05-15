def solution(array, comands):
    answer = []
    for i in comands:
        start = i[0]-1
        end = i[1]
        tmp = array[start:end]
        tmp.sort()
        idx = i[2]-1
        data = tmp[idx]
        answer.append(data)
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))
