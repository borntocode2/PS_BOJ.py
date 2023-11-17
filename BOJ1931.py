N = int(input())
room = [[] for i in range(N)]
count = 1
fk = 0
k = 1
temp = 0
for i in range(N):
    a, b = map(int, input().split())
    room[i].append(a)
    room[i].append(b)
    
room.sort(key = lambda x : x[1]) # key = lambda x : x[] X기준으로 정렬

while k < N:
    if room[fk][1] <= room[k][0]:
        count += 1
        fk = k
    k += 1
print(count)