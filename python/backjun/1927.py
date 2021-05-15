import sys
import heapq

N = int(input())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num !=0:
        heapq.heappush(heap,num)
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(0)
print(heap)

