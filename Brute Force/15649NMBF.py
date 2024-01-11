# 1부터 N 까지 자연수 중에서 중복 없이 M개를 고른 수열 
# nPm 순열 

def dfs(n, lst):
  
    if n == M: 
        ans.append(lst)
        return
    
    for j in range(1, N+1):
        if visits[j] == 0:          
            visits[j] = 1
            dfs(n+1, lst+[j])
            visits[j]=0
    
N, M = map(int, input().split())
ans = [] 
visits = [0]*(N+1) 

dfs(0, [])
for lst in ans:
    print(*lst)

