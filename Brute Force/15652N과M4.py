# 비내림차순과 오름차순의 차이점 = 오름차순은 인접한 인덱스가 같을 수도 있다는 명제가 확실치 않음
N, M = map(int, input().split())
answer = []

def dfs(m, lst, I):
   
    if m == M-1:
        answer.append(lst)
        return
    for j in range(I, N+1):
        dfs(m+1, lst+[j], j)

for i in range(1, N+1):
    dfs(0, [i], i)

for i in answer:
    print(*i)