# 숫자 하나가 추가될 때 마다의 리스트의 중간 값을 추가한다.
# 최댓값 힙 [a, b, c, d] 최솟값 힙 [e, f, g, h] 에서 d를 출력하도록 해야한다.
import heapq as hq
import sys
left_hip = []
right_hip = [] # maxheap
input = sys.stdin.readline
N = int(input())

for i in range(N):
    a = int(input())
    if i == 0:
        hq.heappush(left_hip, -a)
        print(-left_hip[0])
        continue
    if i == 1:
        hq.heappush(right_hip, a)
        if -left_hip[0] > right_hip[0]:
            hq.heappush(right_hip, -hq.heappop(left_hip))
            hq.heappush(left_hip, -hq.heappop(right_hip))
            print(-left_hip[0])
            continue
        else:
            print(-left_hip[0])
            continue

    elif i % 2 == 0:
        dot = right_hip[0]
        if dot < a:
            hq.heappush(left_hip, -a)
            b = hq.heappop(right_hip)
            c = hq.heappop(left_hip)
            hq.heappush(left_hip, -b)
            hq.heappush(right_hip, -c)
        else:
            hq.heappush(left_hip, -a)
    else:
        dot = left_hip[0]
        hq.heappush(right_hip, a)
        if -dot > a:
            b = hq.heappop(left_hip)
            c = hq.heappop(right_hip)
            hq.heappush(right_hip, -b)
            hq.heappush(left_hip, -c)

    print(-left_hip[0])
#-10000 10000 100 -100 1 -1 -1 1 0 3 1
        

#1
#5
#2
#10
#-99
#7
#5
        #  -99 1
# 1 1 2 2 2 2 5
# 5 2