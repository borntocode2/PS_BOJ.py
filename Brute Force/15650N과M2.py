N, M = map(int, input().split())
answer = []
visits = [0 for _ in range(N+1)]

if N == M:
    for i in range(1, N+1):
        answer.append(i)
    print(*answer)
    exit(0)

def dfs(m, lst):
    global j
    if m == M-1:
        answer.append(lst)
        return
    for i in range(j, N+1):
        if visits[i] == 0:
            visits[i] = 1
            dfs(m+1, lst+[i]) #재귀에서는 visits[i] = 0을 해주어야 되고, 본문에서는 return 해야한다.
            visits[i] = 0
    


for j in range(1, N+1):
    visits[j] = 1
    dfs(0, [j])



print(*answer)


