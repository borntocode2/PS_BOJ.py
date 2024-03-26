N = int(input())
MAP = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for i in range(K):
    a, b = map(int, input().split())
    MAP[a][b] = 1
