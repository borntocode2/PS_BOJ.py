# input/output ex) ["12", "123", "345"]
# 12는 123의 접두사이기 때문에 False 
# 접두사가 없으면 True
# level2
# 100만개의 케이스 중 2중반복문으로 돌리기에는 벅참
# 하나의 접두사를 pick한 후에 돌리면 좀 낫겠는데 100만개의 접두사를 검사해야하니..

# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if str(phone_book[i]) == str(phone_book[i+1])[:len(str(phone_book[i]))]:
#             answer = False
#         print(str(phone_book[i+1])[:len(str(phone_book[i]))])
#     return answer 
def solution(phone_book):
    if len(phone_book) == 1:
        return True
    
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: #or // if phone_book[i+1].startswith(s):
            answer = False  
    return answer
print(solution(['1', '23', '234']))