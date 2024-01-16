N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
visits = [0 for _ in range(N+1)]
arr.sort()

def dfs(m, lst):
    if m == M-1:
        answer.append(lst)
        return
    
    for j in range(N):
        if visits[j] == 0:
            visits[j] =1
            dfs(m+1, lst+[arr[j]])
            visits[j] = 0

for i in range(N):
    visits[i] = 1
    dfs(0, [arr[i]])
    visits[i] = 0

for i in answer:
    print(*i)




