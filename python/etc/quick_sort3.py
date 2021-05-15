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

def quickSort(arr,cnt):
    pivot = 0
    left, middle, right = [], [], []
    #배열이 1보다 크면 정렬 진행
    if len(arr) > 1:
        n = len(arr) - 1
        # 피벗 기준 랜덤으로 설정
        idx = random.randint(0, n)
        pivot = arr[idx]
        # 배열
        for i in arr:
            #피벗이 arr의 요소가 피벗보다 크면 right에 추가, 피벗보다 작으면 left에 추가 피벗과 같으면 middle에 추가
            if i >pivot:
                right.append(i)
                cnt.append(1)
            elif i<pivot:
                left.append(i)
                cnt.append(1)
            elif i == pivot:
                middle.append(i)
                cnt.append(1)
            else:
                pass
            #재귀함수를 사용하여 배열을 left,rigth를 quicksort를 진행시켜 값을 추출
        return quickSort(left,cnt) + middle + quickSort(right,cnt)
    #배열이 1보다 작거나 같으면 반환
    else:
        return arr

def main():
    arr = create_RandomList()
    cnt = []
    print(arr)
    start = time.time()
    arr2 = quickSort(arr,cnt)
    print("time :", time.time() - start)
    print(len(set(arr2)))
    print(len(cnt))


if __name__ == "__main__":
    main()
