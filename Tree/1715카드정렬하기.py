N = int(input())
arr = []
answer = []
for i in range(N):
    arr.append(int(input()))


tanswer = arr[0]

if N == 1:
    print(tanswer)
    exit(0)


for i in range(1, N):
    tanswer = tanswer + arr[i]
    answer.append(tanswer)
print(sum(answer))
