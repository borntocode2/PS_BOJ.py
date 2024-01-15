N, M = map(int, input().split())
answer = []

def dfs(m, lst, i):
    if m == M-1:
        answer.append(lst)
        return
    for j in range(i+1, N+1):
        dfs(m+1, lst+[j], j)


for i in range(1, N+1):
    dfs(0, [i], i)

for ans in answer:
    print(*ans)
