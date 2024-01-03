from collections import deque
dq = []
dq = deque()
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
N = int(input())    
for _ in range(N):
    l = int(input())
    cx, cy = map(int, input().split()) # 현재 내 좌표
    fx, fy = map(int, input().split()) # 가야할 좌표
    my_map = [[0 for _ in range(l)] for _ in range(l)]
    visits = [[0 for _ in range(l)] for _ in range(l)]
    my_map[fx][fy] = 1
    dq.append([cx,cy])
    visits[cx][cy] = 1
    if fx == cx and fy == cy:
        print(0)
        continue
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >= 0 and ny >= 0 and nx < l and ny < l:
                if my_map[nx][ny] == 0 and visits[nx][ny] == 0:
                    dq.append([nx,ny])
                    visits[nx][ny] = visits[x][y] + 1
                elif my_map[nx][ny] == 1:
                    print(visits[x][y])
                    my_map.clear()
                    visits.clear()
                    dq.clear()
                    break
        else:
            continue
        break



                



