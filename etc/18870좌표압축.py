N = int(input())
origin = list(map(int, input().split()))
origin_sorted = sorted(set(origin)) #오름차순정렬과 중복제거
origin_answer = []

# 이제 origin_sorted의 값들이 가지는 인덱스가 origin에 있는 값들을 인덱싱한 리스트를 만들어야한다.
origin_dictionary = {j : i for i, j in enumerate(origin_sorted)}
# origin_dictionary = { 5: 1, 3: 0}
# origin_dictionary[5] = 1
print(origin_dictionary)
for i in origin:
    origin_answer.append(origin_dictionary[i])

print(*origin_answer) 



