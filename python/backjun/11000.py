import heapq
import sys

N = int(sys.stdin.readline().rstrip("\n"))
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip("\n").split())))
arr.sort(key=lambda x:x[0])

heap = []
heapq.heapify(heap)
heapq.heappush(heap,arr[0][1])

for i in range(1,N):
    if heap[0] <= arr[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappush(heap, arr[i][1])
print(len(heap))
