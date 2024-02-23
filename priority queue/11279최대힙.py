import sys
import heapq
input = sys.stdin.readline
arr = []
N = int(input())
for i in range(N):
    a = int(input())

    if a == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -a)
