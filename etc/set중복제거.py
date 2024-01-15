lst = [1, [1, 2], [2, 1]] # 리스트 형태의 lst

set_lst = set() # 중복제거를 위해 set형태의 set_lst
list_lst = [] # 중복제거한 set_lst 를 다시 리스트형태로 바꿔주기 위한 list_lst


for i in lst: # lst를 set형태의 set_lst에 담아주는 과정
    if isinstance(i, list): # isinstance 함수. 형태를 알려줌
        set_lst.add(tuple(sorted(i))) # 순서와 상관없이 중복된 값을 제거하려면 sort한 iterable객체를 tuple로 추가해준다
    else:
        set_lst.add(i)

for i in set_lst: #set형태의 set_lst를 list형태인 list_lst에 담아주는 과정 
    if isinstance(i, tuple):
        list_lst.append(list(i))
    else:
        list_lst.append(i)

print(list_lst)