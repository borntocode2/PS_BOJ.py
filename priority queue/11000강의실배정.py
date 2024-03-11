import heapq as hq
N = int(input())
time = 0
hip = []
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()
hq.heappush(hip, arr[0][1])

for i in range(1, N):
    if arr[i][0] >= hip[0]:
        hq.heappush(hip, arr[i][1])
        hq.heappop(hip)
    else:
        hq.heappush(hip, arr[i][1])

print(len(hip))
