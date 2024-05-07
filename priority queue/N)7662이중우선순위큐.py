import heapq as hq
T = int(input())


for cases in range(T):
    N = int(input())
    checkheap = [False] * [2147483649]
    answer = []
    maxheap = []
    minheap = []
    for i in range(N):
        A = list(input().split())
        action = A[0]
        number = int(A[1])
    
        if action == "I": # I = in 연산일 때,
            hq.heappush(minheap, number)
            
            hq.heappush(maxheap, -number)
        else:             # D = delete 연산일 때, 1이면 최댓값, -1면 최솟값
            if len(maxheap) > 0 and len(minheap) > 0:
                if number == 1:
                    hq.heappop(maxheap)
                else:
                    hq.heappop(minheap)
                    
            else:
                continue
    if len(maxheap) > 0 and len(minheap) > 0:
        answer.append(-hq.heappop(maxheap))
        answer.append(hq.heappop(minheap))
    else:
        print("EMPTY")
        break
    print(*answer)
'''
2     
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333

'''
2     
7
