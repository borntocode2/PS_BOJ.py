import heapq as hq
import sys 
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    a = int(input())
    if a == 0:
        origin, second = hq.heappop(arr)
        print(origin)
    else:
            hq.heappush(arr, (a, abs(a)))
