#토요일에 할 것
import random
import time

def create_random_num(a,num):
    num = num* random.randint(1,9)+random.randint(0,9)
    if  num in a:
        return create_random_num(a,num)
    else:
        a.append(num)
        return a

def create_RandomList():
    a = []
    for i in range(1,1025):
        a = create_random_num(a,i)
    return a


def heapify(Arr,index,size,cnt):
    #부모 노드 지정
    p = index
    #자식 노드 지정
    left = index*2 +1
    right = index*2 +2
    # 부모 노드가 왼쪽 자식 노드보다 작으면 교환
    if left < size and Arr[left] > Arr[p]:
        p = left
    #부모 노드가 오른쪽 자식 노드보다 작으면 교환
    if right < size and Arr[right] > Arr[p]:
        p = right
    # 값 변경
    if  p != index:
        #값이 다른 경우 index의 값 바꿔주기
        # 값 변경시 Arr[p]에는 부모의 값이 들어가며 Arr[index]에는 비교해서 나온 자식 노드의 값이 들어감
        Arr[p],Arr[index] = Arr[index],Arr[p]
        #값을 비교 했기에 1 추가
        cnt.append(1)
        # 바뀐 값의 자식도느와 또 비교하여 작으면 교체가 진행됨
        heapify(Arr,p,size,cnt)

def heap_sort(Arr,cnt):
    #길이 설정
    n = len(Arr)
    #haepify 시작 지점 설정
    start_index = (n //2) -1
    #Build max-heap 생성
    for i in range(start_index,-1,-1):
        heapify(Arr,i,n,cnt)
    # heap 정렬 진행
    for i in range(n-1,0,-1):
        Arr[0],Arr[i] = Arr[i],Arr[0]
        heapify(Arr,0,i,cnt)

def main():
    arr = create_RandomList()
    start = time.time()
    cnt = []
    heap_sort(arr,cnt)
    print("time :", time.time() - start)
    print(len(cnt))
    # print(arr)

if __name__ == "__main__":
    main()




