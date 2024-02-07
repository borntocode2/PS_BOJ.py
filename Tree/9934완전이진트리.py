K = int(input())
Nodes = list(map(int, input().split()))
N = pow(2,K) - 1 # N이 3이라면 7개의 인덱스를 가지는 빈 배열 생성
Tree_emt = [[] for _ in range(N)] # 탐색 할 빈 트리
visits = [0 for _ in range(N+1)]
flag = 0
Tree_ans = [[] for _ in range(K)]

def dfs(idx):
    global flag
    if idx <= N and idx > 0: #탐색할 인덱스가 N의 범위 안에 들어온다면,
        if visits[idx] == 0:
            dfs(idx * 2)
            Tree_emt[idx-1] = Nodes[flag]
            flag += 1
            dfs((idx * 2) + 1)
            visits[idx] = 1
dfs(1)
flag = 1
for i in range(1, N+1):
    if i >= pow(2, flag):
        flag += 1
    Tree_ans[flag-1].append(Tree_emt[i-1])
        

for i in range(K):
    print(*Tree_ans[i])

