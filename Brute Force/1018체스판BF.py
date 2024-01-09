N, M = map(int, input().split())
Chesspan = []
fixdot = 0
mindot = 1000000
fixed_N = N - 7
fixed_M = M - 7

# x = 0 y = 5
# BBBWBWBW 1
# BBBBWBWB 6
# BBBWBWBW 1
# BBBBWBWB 6
# BBBWBWBW 1
# BBBBWBWB 6
# BBBWBWBW 1
# BBBBWBWB 6
def BF(x, y):
    global fixdot
    fixdot = 0
    for i in range(8):
        for j in range(8):
            if Chesspan[i][y] == "B":
                if j % 2 == 0:
                    if Chesspan[i][y+j] != "B":
                        fixdot += 1
                else:
                    if Chesspan[i][y+j] != "W":
                        fixdot += 1
            else:
                if j % 2 == 0:
                    if Chesspan[i][y+j] != "W":
                        fixdot += 1
                else:
                    if Chesspan[i][y+j] != "B":
                        fixdot += 1


                        
        
for i in range(N):
    Chesspan.append(input())

for i in range(fixed_N):
    for j in range(fixed_M):
        BF(i,j)
        mindot = min(mindot, fixdot)
print(mindot)