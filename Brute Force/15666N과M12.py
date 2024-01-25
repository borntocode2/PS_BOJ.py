N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
temp_ans = set()
lst_ans = []
arr.sort()

def dfs(m, lst, k):
    if m == M-1:
        ans.append(lst)
        return
    
    for j in range(k, N):
        dfs(m+1, lst+[arr[j]], j)

for i in range(N):
    dfs(0, [arr[i]], i)

for i in ans:
    if isinstance(i, list):
        temp_ans.add(tuple(i))

set_ans = sorted(temp_ans)

for i in set_ans:
    if isinstance(i, tuple):
        lst_ans.append(list(i))

for i in lst_ans:
    print(*i)

