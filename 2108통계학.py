from collections import Counter
nums = []
answer = []
N = int(input())
for i in range(N):
    nums.append(int(input()))

#평균값 탐색
Ever_num = sum(nums) / len(nums)
answer.append(round(Ever_num))

#중앙값 탐색
if len(nums) >= 2:
    nums.sort()
    Middle_num = nums[len(nums)//2]
    answer.append(Middle_num)
else:
    answer.append(nums[0])

#최빈값 탐색
if len(nums) >= 2:
    if Counter(nums).most_common(1)[0][1] == Counter(nums).most_common(2)[1][1]:
        Alot_num = Counter(nums).most_common(2)[1][0]
    else:
        Alot_num = Counter(nums).most_common(1)[0][0]
    answer.append(Alot_num)
else:
    answer.append(nums[0])

#범위 탐색 (최댓값,최솟값)
Range_num = max(nums) - min(nums)
answer.append(Range_num)

for i in range(4):
    print(answer[i])
print(round(2.7))