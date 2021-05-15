import heapq


def solution(scoville,K):
    heap = []
    answer = 0
    for i in scoville:
        heapq.heappush(heap,i)
    
    while len(heap) != 0:
        if heap[0] > K:
            return answer
        # 값을 늘려주는 일을 할 예정
        a = heapq.heappop(heap)
        if len(heap) !=0:
            b = heapq.heappop(heap)
            heapq.heappush(heap,a+(b*2))
        answer += 1
    return -1
