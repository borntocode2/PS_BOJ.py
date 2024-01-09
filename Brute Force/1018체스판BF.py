N, M = map(int, input().split())
Chesspan = []
answerdot = 10000
fixed_N = N - 7
fixed_M = M - 7
# BBBWBWBW 00 02 04 06 // 01 03 05 07
# BBBBWBWB 10 12 14 16 // 11 13 15 17
# BBBWBWBW 20 22 24 26 // 21 23 25 27
# BBBBWBWB 30 32 34 36 // 31 33 35 37




def BF(x, y):
    global coldot, rowdot, realdot
    coldot = 0
    rowdot = 0
    realdot = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if Chesspan[x+i][y+j] != "W":
                    coldot += 1
                else:
                    rowdot += 1
            else:
                if Chesspan[x+i][y+j] != "B":
                    coldot += 1
                else:
                    rowdot += 1
                    
    realdot = min(coldot, rowdot)

                        
        
for i in range(N):
    Chesspan.append(input())

for i in range(fixed_N):
    for j in range(fixed_M):
        BF(i,j)
        answerdot = min(answerdot, realdot)
        
print(answerdot)


