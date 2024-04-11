def Snake(a, b):
    global time, turn, x, y
    
    if b == "D":
        turn += 1
    else:
        turn -= 1

    if turn < 0:
        turn = 3
    if turn > 3:
        turn = 0

    for k in range(a):
        if x+dx[turn] < N or y+dy[turn] < N or x+dx[turn] >= 0 or y+dy[turn] >= 0 or MAP[x+dx[turn]][y+dy[turn]] >= 0:
            if MAP[x+dx[turn]][y+dy[turn]] == 1:
                MAP[x+dx[turn]][y+dy[turn]] = -1
            else:
                x = x + dx[turn]
                y = y + dy[turn]
                time += 1
                MAP.remove(-1)

        else:
            print(time)
            exit(0)

        if b == "R":
            turn += 1
        else:
            turn -= 1

        

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N = int(input())
MAP = [[0 for _ in range(N)] for _ in range(N)]
time = 0
turn = 0
x = 0
y = 0
K = int(input())

for i in range(K): #사과 위치 저장
    a, b = map(int, input().split())
    MAP[a][b] = 1

L = int(input()) # 뱀의 이동정보 저장

for i in range(L):
    a, b = input().split()
    if i == 0:
        Snake(int(a), 0)
    else:
        Snake(int(a), b)
    