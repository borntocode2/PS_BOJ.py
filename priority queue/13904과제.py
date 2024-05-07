import heapq
arr = []
N = int(input())
for i in range(N):
    arr.append(list(map(int,input().split())))

if len(arr) >= 2:
    arr.sort(key = lambda x : x[1], reverse = True)

if len(arr) == 1:
    print(arr[0][1])
    exit(0)

day_list = [0 for i in range(1001)]

for i in range(N):
    if day_list[arr[i][0]-1] == 0: # 만약 day_list의 해결하려는 과제 날짜가 비어있다면
        day_list[arr[i][0]-1] = arr[i][1]
    else:
        j = 1
        while arr[i][0]-j >= 0:
            if day_list[arr[i][0]-j] == 0:
                day_list[arr[i][0]-j] = arr[i][1]
                break
            j += 1

print(sum(day_list))

    
    