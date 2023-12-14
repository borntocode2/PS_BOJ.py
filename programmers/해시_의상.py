# 딕셔너리자료형은 해당 키가 가지는 값이 1개 뿐이여야 해서, 다양한 의상의 이름을 다루지 못함.
# 리스트자료형으로 마지막인덱스(의상의 종류)로 같은 의상의 종류를 묶으려했으나 "문자열"자료형을 결국 다뤄야 할 것 같음.
# 튜플? 자료형으로 하면 된다는데 익숙치 않음.

def solution(clothes):
    cnt = 0
    answer = 0
    alist = [[]for _ in range(30)]
    for i in clothes:
        if 


    return answer