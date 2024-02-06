N = int(input())
import sys
sys.setrecursionlimit(10**6)
relations = [[] for _ in range(N+1)]
parents = [[] for _ in range(N+1)]
visits = [0 for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

def dfs(idx):
    for i in relations[idx]:
        if visits[i] == 0:
            parents[i].append(idx)
            visits[i] = 1
            dfs(i)

visits[1] = 1
dfs(1)
for i in range(2, N+1):
    print(*parents[i])
