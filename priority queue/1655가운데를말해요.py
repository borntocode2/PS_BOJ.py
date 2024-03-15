# 숫자 하나가 추가될 때 마다의 리스트의 중간 값을 추가한다.
# 최댓값 힙 [a, b, c, d] 최솟값 힙 [e, f, g, h] 에서 d를 출력하도록 해야한다.
import heapq as hq

hip = []
N = int(input())

for i in range(N):
    a = int(input())
    hq.heappush(hip, a)
    
    print(hip)
    if len(hip)%2 == 0:
        print("가운데 수는: ", min(hip[len(hip) // 2], hip[(len(hip) // 2) - 1]))

    else:
        print("가운데 수는: ", hip[len(hip) // 2])

#7
        
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