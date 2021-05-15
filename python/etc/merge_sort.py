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

def merge_sort(arr,cnt):
    #배열이 1보다 작거나 같으면 요소가 하나이기에 배열을 반환
    # 비교할 값이 없기에 cnt.append(1) 진행 x
    if len(arr) <= 1:
        return arr
    #중간 지점 찾기
    mid = len(arr)//2
    # 중간 지점 기준으로 왼쪽부분 merger_sort 시행 
    left = merge_sort(arr[:mid],cnt)
    # 중간 지점 기준으로 오른쪽부분 merger_sort 시행
    right = merge_sort(arr[mid:],cnt)
    #sort후 left와 right를 합쳐서 배열 재구성
    return merge(left, right,cnt)

#수정해보기
def merge(left, right,cnt):
    #merge한 결과를 돌린 배열 생성
    result = []
    #left와 right의 배열의 길이가 모두 0이 아닌 이상 계속 실행
    while len(left) > 0 or len(right) > 0:
        #left 와 right의 값을 비교해 순서대로 넣기
        #left right둘 중하나라도 길이가 0이 아닐떄 비교
        if len(left) > 0 and len(right) > 0:
            #left의 값이 right보다 작다면 result에 left의 첫 요소 값 넣기
            if left[0] <= right[0]:
                result.append(left[0])
                #left의 첫요소를 넣었기에 값 제거
                left = left[1:]
                # 비교하면 1을 cnt 배열에 저장
                cnt.append(1)
                #right의 값이 left보다 작다면 result에 right의 첫 요소 값 넣기
            else:        
                result.append(right[0])
                #right의 첫요소를 넣었기에 값 제거
                right = right[1:]
                # 비교하면 1을 cnt 배열에 저장
                cnt.append(1)
        #right가 0이고 left가 0이 아닐 경우
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        #left가 0이고 right가 0이 아닐 경우
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def main():

    arr = create_RandomList()
    #비교한 횟수를 나타내기 위한 cnt
    cnt = []
    start = time.time()
    arr1 = merge_sort(arr,cnt)
    print("time :", time.time() - start)
    print(len(set(arr)))
    print(len(cnt))

if __name__ == "__main__":
    main()
