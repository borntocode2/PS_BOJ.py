N, M = map(int,input().split())
arr = list(map(int, input().split()))
answer = []
arr.sort()
def dfs(m, lst):
    if m == M-1:
        answer.append(lst)
        return
    for j in arr:
        dfs(m+1, lst + [j])

for i in arr:
    dfs(0, [i])

for i in answer:
    print(*i)
