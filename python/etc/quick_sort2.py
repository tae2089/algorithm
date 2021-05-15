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

def sort(arr,p, r,cnt):
    if p >= r:
        return
    q = partition(arr,p, r,cnt)
    sort(arr,p, q - 1,cnt)
    sort(arr,q, r,cnt)

def partition(arr,p, r,cnt):
    #pivot 중간 지정
    pivot = arr[(p + r) // 2]
    #p부터 r까지 정렬 진행
    while p <= r:
        #pivot기준으로 처음부분부터 증가시키면서 pivot보다 큰값 찾기
        while arr[p] < pivot:
            p += 1
        #pivot 기준으로 끝부분부터 감소시키면서 pivot보다 작은 값 찾기
        while arr[r] > pivot:
            r -= 1
        if p <= r:
            #pivot 기준으로 왼쪽에 작은값이 있어야 하며 오른쪽에 큰값이 있어야 함
            # 값변경을 통해 위 코멘트 형식으로 변경
            arr[p], arr[r] = arr[r], arr[p]
            # 값 변경 후 인덱스의 요소 증감 시행
            p, r = p + 1, r - 1
            #값 비교를 통해 요소 증가
            cnt.append(1)
    return p

def main():
    cnt = []
    #arr = [1,3,2,4]
    arr = create_RandomList()
    print("main",arr)
    start = time.time()
    sort(arr, 0, len(arr) - 1,cnt)
    print("time :", time.time() - start)
    print(len(set(arr)))
    print(len(cnt))

if __name__ == "__main__":
    main()
