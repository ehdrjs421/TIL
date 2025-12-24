# def len_func(list):
#     answer = 0
    
#     while(bool(list)):
#         list.pop()
#         answer += 1
        
#     return answer

# numbers = [2,3,2,1,3,5,6]
# print(len_func(numbers))

# 자연수 N을 입력받아, N줄까지 별을 출력하는 함수를 만드시오.
# 첫 번째 줄은 별이 1개이며, N번째 줄은 N개의 별이 찍혀야 합니다.

# ex) 만약 N이 3 이라면?
# *
# **
# ***

# N = int(input())

# def print_stars(N):
#     # pass를 지우고 로직을 작성합니다.
#     for i in range(N):
#         a = '*'*(i+1)
#         print(a)
        
# print_stars(N)


# 리스트 정렬
# 주어진 2차원 리스트를 기준에 따라서 정렬하시오.
# (1) [앞쪽, 뒤쪽] 이라고 할 때, 뒤 쪽이 '작은' 순서로 정렬하되 
# (2) 만약 같다면 앞쪽이 '큰' 순서대로 정렬하시오.
nums = [[70, 30], 
        [70, 10], 
        [20, 30], 
        [50, 90], 
        [40, 80], 
        [80, 90], 
        [10, 60]]

nums_r = sorted(nums, key = lambda x:(x[1],-x[0]))
print(nums_r)