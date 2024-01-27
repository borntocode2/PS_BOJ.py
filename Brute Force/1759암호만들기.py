# 최소한개의 모음(a e i o u), 최소두개의 자음
# 정렬
# L = 암호의 글자수, C = 주어진 알파벳
L, C = map(int, input().split())
consonant = ["a", "e", "i", "o", "u"] # 모음은 vowel

arr = list(input().split())
visits = [0 for _ in range(C+1)]
ans = []
answer = []
arr.sort()

def dfs(m, lst, k):
    if m == L-1:
        answer.append(lst)
        return
    
    for j in range(k, C):
        dfs(m+1, lst + [arr[j]], j+1)

for i in range(C):
    dfs(0, [arr[i]], i+1)


for lst in answer: #모음이 1개이상, 자음 2개이상이면 ans에 값을 추가
    cnt_con = 0
    cnt_vowel = 0
    for j in lst:
        if j in consonant:
            cnt_con += 1
        else:
            cnt_vowel += 1
    if cnt_con >= 1 and cnt_vowel >= 2:
        ans.append(lst)

for i in ans:
    print(*i, sep = "") # 출력한 값에  공백이 있다면 sep ="" 으로 없애주면 됨 -> sep은 none or string값으로 만 가능

