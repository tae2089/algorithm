array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []
for command in commands:
    # print(command)
    answer.append(sorted(array[command[0]-1:command[1]])[command[-1]-1])
    # answer.append(array[command[0]:command[1]][command[-1]-1])
    # print(answer)
    # print(a)
print(answer)