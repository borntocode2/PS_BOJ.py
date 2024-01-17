N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer= []

if N == M:
    print(*arr)
    exit(0)

def dfs(m, lst, I):
    if m == M-1:
        answer.append(lst)
        return
    for j in range(I+1, len(arr)):
        dfs(m+1, lst+[arr[j]], j)


for i in range(len(arr)):
    dfs(0, [arr[i]], i)

for i in answer:
    print(*i)