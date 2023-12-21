# N개 줄에 걸쳐 사이트 주소와 비밀번호 입력
# M개 줄에 걸쳐 찾고자하는 사이트 주소 
# 비밀번호 출력

N, M = map(int, input().split())
dict = {}
find_Address = []
for i in range(N):
    Address, Password = map(str, input().split()) # N개 줄에 걸쳐 주소와 비번이 입력된다
    dict[Address] = Password # 주소와 비번들을 딕셔너리 자료형의 dict에 저장해줌

for i in range(M):
    find_Address.append(input()) # 찾고자하는 주소들을 입력받음

for i in find_Address:
    print(dict[i])

