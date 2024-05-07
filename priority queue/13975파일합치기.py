import heapq as hq #1715카드정렬하기랑 비슷한 문제.
hip = []            # heap구조를 사용해 최소비용을 구하는 알고리즘을 잘 기억해둘 것.
answer = []         # 두 개 합치고 -> 합을 push -> 두 개 합치고
T = int(input())

for cases in range(T):
    hip = []
    sum_temp = 0
    N = int(input())
    files = list(map(int,input().split()))

    for j in files:
        hq.heappush(hip, j)
    while len(hip) >= 2:
        a = hq.heappop(hip)
        b = hq.heappop(hip)
        temp = a + b
        
        sum_temp += temp
        hq.heappush(hip, temp)
    answer.append(sum_temp)

for i in answer:
    print(i)

            

        