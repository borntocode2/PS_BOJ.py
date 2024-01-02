N = int(input())
N_numbers = map(int,input().split())
M = int(input())
M_numbers = map(int, input().split())
answer = []
dict = {}
for i in N_numbers:
    if str(i) in dict:
        dict[str(i)] += 1
    else:
        dict[str(i)] = 1
for j in M_numbers:
    if str(j) in dict:
        answer.append(dict[str(j)])
    else: 
        answer.append(0)
print(*answer)

