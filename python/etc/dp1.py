#sugar derivery 백준 2839


def solution(data):
    dev = [5, 3]
    cnt = 0
    cnt_list = []

    #조건문 설정
    is_namugi1 = False
    is_namugi2 = False

    for j in dev:
        if data % j == 0:
            a = data / j
            cnt_list.append(int(a))
            is_namugi1 = True

    for i in dev:
        value = data//i
        cnt += value
        data = data - (value*i)

    if data == 0:
        cnt_list.append(int(cnt))
        is_namugi2 = True
    
    cnt_list.sort()

    if  is_namugi1|is_namugi2 :
        return cnt_list[0]
    else:
        return -1


def main():
    data = 18
    output = solution(11)
    print(output)

if __name__ == '__main__':
    main()
