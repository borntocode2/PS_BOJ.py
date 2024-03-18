# 숫자 하나가 추가될 때 마다의 리스트의 중간 값을 추가한다.
# 최댓값 힙 [a, b, c, d] 최솟값 힙 [e, f, g, h] 에서 d를 출력하도록 해야한다.
import heapq as hq
import sys
input = sys.stdin.readline
left_hip = []
right_hip = [] # maxheap

N = int(input())

for i in range(N):
    a = int(input())
    if len(left_hip) >= 1:
        dot = left_hip[0]
        if i % 2 == 0:
            hq.heappush(left_hip, -a)
            if -dot <= a:
                right = hq.heappop(right_hip)
                hq.heappush(right_hip,-hq.heappop(left_hip))
                hq.heappush(left_hip, right)


        else:
            hq.heappush(right_hip, a)
    else:
        hq.heappush(left_hip, -a)
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