import heapq as hq

N = int(input())
MAP = [[0 for _ in range(N)] for _ in range(N)]
time = 0
heap = []
K = int(input())

for i in range(K): #사과 위치 저장
    a, b = map(int, input().split())
    MAP[a][b] = 1
L = int(input())

for i in range(N): #뱀의 방향 정보
    arr = input().split()
    hq.heappush(heap, arr)

