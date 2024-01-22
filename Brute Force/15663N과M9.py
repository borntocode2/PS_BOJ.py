#중복 된 수열을 없애야 한다.
# 첫 번째 방법 -> set함수 
# 두 번째 방법 -> 이전에 추가된 수열의 끝자리와 같다면 추가 X

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
set_ans = set()
lst_ans = []
visits = [0 for _ in range(N+1)]
arr.sort()



def dfs(m, lst):
    if m == M-1:
        ans.append(lst)
        return
    for j in range(N):
        if visits[j] == 0:
            visits[j] = 1
            dfs(m+1, lst + [arr[j]])
            visits[j] = 0

for i in range(N):
    visits[i] = 1
    dfs(0, [arr[i]])
    visits[i] = 0

# list -> set -> list 과정을 통해 중복제거

for i in ans:
    if isinstance(i, list):
        set_ans.add(tuple(i))

sorted_set = sorted(set_ans)  # set자료형은 순서르 보장X sorted함수를 통해 순서보장해주자

for i in sorted_set:
    if isinstance(i, tuple):
        lst_ans.append(list(i))

for i in lst_ans:
    print(*i)