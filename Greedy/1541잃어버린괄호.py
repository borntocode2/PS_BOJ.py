strArr = list(input().split("-"))
tempArr = []
intArr = []
for i in strArr:
    tempArr.append(i.split("+"))

for i in tempArr:
    sum = 0
    for j in i:
        sum += int(j) 
    intArr.append(sum)

answer = intArr[0]

if len(intArr) > 1:
    for i in range(1,len(intArr)):
        answer -= intArr[i]

print(answer)

