N, M = map(int, input().split()) # M = 폐업 안시킬 치킨집 갯수
city = []
coord = [] # coordinate has a chiken resturants address(coordinate)
coord_house = []
coord_cases = []
answer = []


for i in range(N):
    arr = list(map(int, input().split()))
    city.append(arr)

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            coord.append([i, j])
        elif city[i][j] == 1:
            coord_house.append([i,j])


coord_number = len(coord)
visits = [0 for i in range(coord_number+1)]

def dfs(m, lst,k):
    if m == M-1:
        coord_cases.append(lst)
        return
    
    for j in range(k, coord_number):
        if visits[j] == 0:
            visits[j] = 1
            dfs(m+1, lst+[coord[j]], j+1)
            visits[j] = 0

for i in range(coord_number):
    visits[i] = 1
    dfs(0, [coord[i]], i+1)
    visits[i] = 0

for i in range(len(coord_house)):
    x, y = coord_house[i]
    
    

