import heapq as hq
hip = []
n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    hq.heappush(hip, (arr[0], arr[1]))

for i in range(n):
    print(hq.heappop(hip))
