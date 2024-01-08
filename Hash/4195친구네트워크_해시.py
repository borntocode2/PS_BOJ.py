N = int(input())
dict = {}
for i in range(N):
    F = int(input())
    dict.clear()                #딕셔너리 초기화
    for j in range(F):
        A, B = map(str, input().split())
        if A not in dict:
            dict[A] = 1
        if B not in dict:
            dict[B] = 1
        print(dict[A]+dict[B])
        temp = dict[A]
        dict[A] += dict[B]
        dict[B] += temp
