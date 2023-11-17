N = int(input())
room = [[] for i in range(N)]
count = 1
fk = 0
k = 1
for i in range(N):
    a, b = map(int, input().split())
    room[i].append(a)
    room[i].append(b)
    
room.sort(key = lambda x : x[1]) # key = lambda x : x[] X기준으로 정렬, x[1]이 다 같은 경우엔 정렬이 제대로 안됨
                                 # ex) (4,4), (3,4), (2,4)
                                 # ex) (3,6), (2,6), (1,6)
while k < N:
    if room[fk][1] <= room[k][0]:
        count += 1
        fk = k
    elif room[fk][0] == room[fk][1]:
        for i in range(fk+1, N-fk):
            if room[fk][1] <= room[i][1]:
                count += 1
                fk = i
                break
    k += 1
    
print(count)