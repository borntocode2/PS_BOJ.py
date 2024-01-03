N,M = map(int, input().split())

relations = [[] for _ in range(M)]

for i in range(M):
    a,b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

break_point = False #DFS함수 안의 글로벌 변수로 지정해서 depth(탐색이 몇번 연속으로 진행됐는지)가 4가 될 때 true함으로써 탐색을 멈출 수 있다.
visits = [False] * 2001 #relations의 노드들을 방문할 때 체크함으로써 오류를 방지할 수 있다. 

def DFS(idx, depth):
    visits[idx] = True
    global break_point
    if depth == 4:
        break_point = True
        return

    for i in relations[idx]: #idx는 DFS함수의 인자값이다. 즉, relations의 노드를 방문하고, 그 노드의 값이 relations의 인덱스가 되어 이어지는지 확인하는 것.
        if visits[i] == False: #방문하지 않았다면, 
            visits[i] = True   #방문처리해주고,
            DFS(i, depth + 1)  #depth를 1더해주고 다음relations로 탐색하러 이동한다.
            visits[i] = False  #이동이 끝나고(depth != 4) DFS함수들이 스택에서 하나씩 없어질 때 체크했던 visits들을 다 해제.

for i in range(M):
    DFS(i, 0)
    visits[i] = False
    if break_point:
        print(1)
        break
else: #for ~ else 구문, for문의 break을 만나지 않고 정상적으로 종료되었을 때 else구문의 코드가 실행된다. 
    print(0)



