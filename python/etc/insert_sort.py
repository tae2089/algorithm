import random
import time


def create_random_num(a, num):
    num = num * random.randint(1, 9)+random.randint(0, 9)
    if num in a:
        return create_random_num(a, num)
    else:
        a.append(num)
        return a

def create_RandomList():
    a = []
    for i in range(1, 1025):
        a = create_random_num(a, i)
    return a


def insert_sort(arr,cnt):
    for i in range(1, len(arr)):
        #기준 값
        to_insert = arr[i]
        j = i
        # 기준 값과 비교하여 하기
        while j > 0 and arr[j - 1] > to_insert:
            arr[j] = arr[j - 1]
            j -= 1 
            cnt.append(1)
        arr[j] = to_insert
    return arr,cnt

def main():
    arr = create_RandomList()
    #arr = [random.randint(0, 1024) for _ in range(1024)]
    # 배열을 통해 총 진행되 갯수 세기
    cnt  =[]
    start = time.time()
    arr,cnt = insert_sort(arr,cnt)
    print("time :", time.time() - start)
    print(arr)
    c = set(arr)
    print(len(c))
    print(len(cnt))

if __name__ == "__main__":
    main()
