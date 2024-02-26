import heapq as hq
N, M = map(int, input().split())
arr = list(map(int, input().split()))
hq.heapify(arr)



for i in range(M):
    a = hq.heappop(arr)
    b = hq.heappop(arr)
    hq.heappush(arr, a+b)
    hq.heappush(arr, a+b)
print(sum(arr))
        
        
# 4 3 3 3
# 6 6 4 3


