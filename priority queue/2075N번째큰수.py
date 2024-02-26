import heapq as hq
N = int(input())
hip = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in arr:
       hq.heappush(hip, -j)

for i in range(N-1):
    hq.heappop(hip)
print(-hq.heappop(hip))
