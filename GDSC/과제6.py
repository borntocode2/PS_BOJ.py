import random

num = random.randint(1, 50)

while 1:
    print("숫자를 입력하세요 >> ")
    X = int(input())

    if X == num:
        print("정답을 맞추셨습니다.")
        break
    elif X > num:
        print(X,"보다 작은 수 입니다.")
    else:
        print(X,"큰 수 입니다.")