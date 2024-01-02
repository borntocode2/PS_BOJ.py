from collections import deque
dq = []
dq = deque()
N = int(input())
arr = []
answer = []
answer = [[] for _ in range(N)]
relations = [[] for _ in range(N)]
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            relations[i].append(j)

for i in range(N):
    for j in range(N):
        flag = 0
        visits = [False] * N
        for k in relations[i]:
            dq.append(k)
            visits[k] = True
        if k == j:
            flag = 1
        while dq:
            if flag == 0:        
                for g in relations[dq.popleft()]:
                    if g == j:
                        flag = 1
                        break

                    if not visits[g]:
                        dq.append(g)
                        visits[g] = True

            else:
                dq.clear()
                break
        if flag == 0:
            answer[i].append(0)
        else:
            answer[i].append(1)
for i in range(N):
    print(*answer[i])
        
         

                    
            






