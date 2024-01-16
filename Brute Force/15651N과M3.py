N, M = map(int,input().split())
answer = []

def dfs(m, lst):
    if m == M-1:
        answer.append(lst)
        return
    for j in range(1, N+1):
        dfs(m+1, lst+[j])

for i in range(1, N+1):
    dfs(0, [i])

for i in answer:
    print(*i)