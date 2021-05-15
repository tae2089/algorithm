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

#값 변경
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A

def quick_sort(A, p, r,cnt):
    if p < r:
        #pivot선정
        q= partitions(A, p, r,cnt)
        #pivot기준 왼쪽 배열 정렬
        quick_sort(A, p, q-1,cnt)
        #pivot기준 오른쪽 배열 정렬
        quick_sort(A, q+1, r,cnt)
    return A

def partitions(A,p,r,cnt):
    #pivot 값 설정
    pivotidx = p
    pivotvalue = A[pivotidx]
    # pivot값을 맨 뒤로 보낸다
    swap(A,pivotidx,r)
    #pivot의 위치 지정
    q = p
    #정렬 진행
    for j in range(p,r):
        #피벗보다 작으면 현 피벗 왼쪽으로 값 이동
        if A[j] <pivotvalue :
            swap(A,j,q)
            q = q+1
            cnt.append(1)
    #마지막 값과 피벗위치에 있는 값 변경
    swap(A, q, r)
    cnt.append(1)
    return q


def main():
    #비교한 횟수를 나타내기 위한 cnt
    cnt = []
    arr = create_RandomList()
    #0부터 배열의 끝을 넣어준다.
    start = time.time()
    arr2 = quick_sort(arr,0,len(arr)-1,cnt)
    print("time :", time.time() - start)
    print(len(set(arr2)))
    print(len(cnt))

if __name__ == "__main__":
    main()
