from collections import deque
N = int(input())
arr = []
dq = []
dq = deque()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
maxcount = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

for k in range(0, 101):
    underwater = [[0 for _ in range(N)] for _ in range(N)] # visits와 함께 추적해줄 물에 잠긴 map, EST initialization
    visits = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= k:
                underwater[i][j] = 1 # 물에 잠김
    
    for i in range(N):
        for j in range(N):
            if visits[i][j] == 0 and underwater[i][j] == 0:
                dq.append([i,j])
                count += 1
                while dq:
                    x, y = dq.popleft()
                    for z in range(4):
                        nx = dx[z] + x
                        ny = dy[z] + y
                        if nx >= 0 and ny >= 0 and nx < N and ny < N and underwater[nx][ny] ==0 and visits[nx][ny] ==0:
                            visits[nx][ny] = 1
                            dq.append([nx, ny])
    maxcount = max(count, maxcount)

print(maxcount)

    




