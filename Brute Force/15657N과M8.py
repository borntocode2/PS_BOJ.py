N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
arr.sort()

def dfs(m, lst, k):
    if m == M-1:
        answer.append(lst)
        return
    
    for j in range(k, N):
        dfs(m+1, lst + [arr[j]], j)



for i in range(N):
    dfs(0, [arr[i]], i)

for i in answer:
    print(*i)