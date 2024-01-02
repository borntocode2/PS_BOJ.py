from collections import deque
N, M, R = map(int, input().split())
relations = [[] for _ in range(N+1)]
visits = [ -1 for _ in range(N+1)]
relations_cnt = [[] for _ in range(N+1)]
cnt = 1
dq = []
dq = deque()
relations_cnt[R].append(cnt)

for i in range(M):
    A,B = map(int, input().split())
    relations[A].append(B)
    relations[B].append(A)

for i in range(1, N+1):
    relations[i].sort()

for i in relations[R]:
    dq.append(i)
    visits[R] = 1


while dq:
    x = dq.popleft()
    if visits[x] == -1:
        cnt += 1
        relations_cnt[x].append(cnt)
        for i in relations[x]:
            dq.append(i)
            visits[x] = 1

for i in range(N+1):
    if visits[i] == -1:
        relations_cnt[i].append(0)
for i in range(1, N+1):
    print(*relations_cnt[i])


    