# 1부터 N 까지 자연수 중에서 중복 없이 M개를 고른 수열 
# nPm 순열 

N, M = map(int,input().split())
answer = []
visits = [0 for _ in range(N+1)]

def DFS(m, lst):
    if m == M:
        answer.append(lst)
        return
    for j in range(1, N+1):
        if visits[j] == 0:
            visits[j] = 1
            DFS(m+1, lst+[j])
            visits[j] = 0

DFS(0, [])

for i in answer:
    print(*i)



