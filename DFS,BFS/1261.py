from collections import deque

dq = deque()



dx = [0, -1, 0 ,1]
dy = [-1, 0, 1, 0]

mymap = []
M, N = map(int, input().split())
visits = [[-1 for _ in range(M)] for _ in range(N)] 


for _ in range(N):
    mymap.append(list(input()))
dq.append([0, 0])
visits[0][0] = 0