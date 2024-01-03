def solution(array, commands):
    answer = []
    answer_list = []
    for i in range(len(commands)):
        start = commands[i][0]
        last = commands[i][1]
        target = commands[i][2] - 1
        
        for j in range(start-1, last):
            answer_list.append(array[j])
            
        answer_list.sort()
        answer.append(answer_list[target])
        answer_list.clear()
    return answer