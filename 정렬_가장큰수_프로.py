def solution(numbers):
    answer_list = []
    answer =''
    for i in numbers:
        if i < 10 and i != 0:
            n = 1
            answer_list.append(i)
        elif i >= 10 and i < 100:
            n = 2
            answer_list.append(i//10)
            answer_list.append(i%10)
        else:
            n = 3
            answer_list.append(i//100)
            answer_list.append((i//10) % 10)
    for i in answer_list:
        answer = answer + str(i)
    return answer
print(solution([1,2,3,4]))
