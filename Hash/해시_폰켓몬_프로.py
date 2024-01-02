def solution(nums):
    
    nums_len = len(nums)
    nums_list = list(set(nums))
    if nums_len // 2 >= len(nums_list):
        answer = len(nums_list)
    else:
        answer = nums_len // 2
    return answer
