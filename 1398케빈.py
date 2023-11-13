from collections import deque
dq = []
dq = deque()
N, M = map(int , input().split())
relations = [[] for _ in range(N+1)]
visits = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    relations[A].append(B)
    relations[B].append(A)  
    # ~~ 인접행렬 저장

def BFS(x):
    ans = 0
    dq.append(x) # 밑에서 1 ~ N 값을 BFS함수호출과 동시에 인자로 넣어주게 됨
    while dq:
        tar = dq.popleft() # 인자로 받은 x 값을 tar변수에 넣어주고, relations[tar]
        for i in relations[tar]:
            if not visits[i] and i != x: 
                dq.append(i) # relations[tar]의 값 중에, 방문 안한 놈들을 dq에다가 넣어줌
                visits[i] = (visits[tar]) + 1 # 몇번의 단계를 거쳐 친구관계인지 확인해주는 visits 설정
    for k in range(1, N+1):
        ans += visits[k] #visits들을 다 합쳐주면 케빈 베이컨 수가 완성
    return ans

res = []
for i in range(1, N+1):
    x= BFS(i)
    res.append(x)
    visits = [0 for _ in range(N+1)]

print(res.index(min(res)) + 1) 






    











