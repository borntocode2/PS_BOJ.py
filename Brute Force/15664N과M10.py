N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
set_ans = set()
reset_ans = set()
lst_ans = []
arr.sort()

if N == M:
    print(*arr)
    exit(0)

def dfs(m, lst, k):
    if m == M-1:
        ans.append(lst)
        return
    
    for j in range(k, N):
        dfs(m+1, lst + [arr[j]], j+1)

for i in range(N):
    dfs(0, [arr[i]], i+1)

for i in ans:
    if isinstance(i, list):
        set_ans.add(tuple(i))

reset_ans = sorted(set_ans)

for i in reset_ans:
    if isinstance(i, tuple):
        lst_ans.append(list(i))

for i in lst_ans:
    print(*i)
