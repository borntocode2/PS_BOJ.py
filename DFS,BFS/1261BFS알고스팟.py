from collections import deque

dq = deque()
dx = [0, -1, 0 ,1]
dy = [-1, 0, 1, 0]

mymap = []
M, N = map(int, input().split())
visits = [[-1 for _ in range(M)] for _ in range(N)] 


for _ in range(N):
    mymap.append(list(int((input()))))
dq.append([0, 0])
visits[0][0] = 0
while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if visits[nx][ny] == -1:
                if mymap[nx][ny] == 1:
                    dq.append([nx,ny])
                    visits[nx][ny] = visits[x][y] + 1
                else:
                    visits[nx][ny] = visits[x][y]
                    dq.appendleft([nx,ny])

print(visits[N -1][M -1])



# def calc(dq):
#     while dq:
#         x, y = dq.popleft()
#         if x == N - 1 and y == M - 1:
#             break
#         print(x, y)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y = dy[i]
#             if nx < 0 or ny < 0 or nx < N or ny < M:
#                 continue
#             if visits[nx][ny] != -1:
#                 continue
#             if mymap[nx][ny] == 1:
#                 visits[nx][ny] = visits[x][y] + 1
#                 dq.append([nx, ny])
#             else:
#                 visits[nx][ny] = visits[x][y]
#                 dq.appendleft([nx, ny])
#     print(visits[N -1][M -1])