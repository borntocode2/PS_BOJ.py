import heapq as hq

n = int(input())
heap = []
system = [ 0 for _ in range(10001)]
for i in range(n):
    arr = list(map(int, input().split()))
    hq.heappush(heap, (-arr[0], arr[1]))


for i in range(n):
    pay, day = hq.heappop(heap)

    while day > 0:
        if system[day] != 0:
            day -= 1
        else:
            system[day] = -pay
            break
print(sum(system))


    
    


               