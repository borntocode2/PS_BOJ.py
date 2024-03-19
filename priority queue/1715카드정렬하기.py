import heapq
heap = []
sum = 0
N = int(input())
for i in range(N):
     heapq.heappush(heap, int(input())) # heapq.heappush 는 변수에 따라 변하지 않는 함수

while len(heap) >= 2:
    a = heapq.heappop(heap)          #heapq.heappop 는 변수에 따라 변하지 않는 함수
    b = heapq.heappop(heap)
    tempsum = a + b
    heapq.heappush(heap, tempsum)
    sum += tempsum


print(sum)
    
#1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

# 1 2 3 4