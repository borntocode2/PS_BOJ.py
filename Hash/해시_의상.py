# 딕셔너리자료형은 해당 키가 가지는 값이 1개 뿐이여야 해서, 다양한 의상의 이름을 다루지 못함.
# 리스트자료형으로 마지막인덱스(의상의 종류)로 같은 의상의 종류를 묶으려했으나 "문자열"자료형을 결국 다뤄야 할 것 같음.
# 튜플? 자료형으로 하면 된다는데 익숙치 않음.

# ........
# clothes 는 리스트이기때문에 순회하면서 clothes[i][-1] 이 딕셔너리에 있는 경우,
# 값 +
# 없는 경우 생성,
# 딕셔너리는 dict[str(clothes)[i][-1]] = count(clothes[i]) 일 듯,
# 경우의 수 생각해볼 
def solution(clothes):
    answer_plus = 0
    answer_multi = 1
    answer = 0
    dict = {}

    for i in range(len(clothes)):
        key = clothes[i][-1] 
        if key in dict:
            origin_value = dict.get(key)
            dict[key] = origin_value + len(clothes[i]) - 1
        else:
            dict[key] = len(clothes[i]) - 1

    for i in dict.values():  # key를 모를 때, 딕셔너리를 순회하면서 값을 확인 할 수 있음.
        answer_multi *= i+1  # 조합
    print(dict)
    answer = answer_multi -1

    return answer
print(solution([["a", "headgear"], ["b", "headgear"], ["c", "eyewear"], ["d", "eyewear"], ["e", "face"], ["f", "face"]]))