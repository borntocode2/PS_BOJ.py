N = int(input())
TimeTable = []
PayTable = []
maxPay = 0 
flag = N

for i in range(N):
    T, P = map(int, input().split())
    TimeTable.append(T)
    PayTable.append(P)

for i in range(N-1, -1, -1):
    if i + TimeTable[i] <= flag:
        flag = i + 1
        

        
        
 