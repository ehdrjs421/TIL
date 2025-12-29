# ## 복습 퀴즈

# users = {
#   'total_user': 3,
#   'information': [
#       {'name': 'alex', 'age':3, 'license':True},
#       {'name': 'june', 'age':7, 'license':False},
#       {'name': 'peter', 'age':4, 'license':False}
#   ]
# }
# information = users['information']
# users_len = users['total_user']
# # Q1. 라이센스가 있는 인원들의 숫자 구하기
# num_lic = 0

# # for i in range(users_len):
# #     dict_inf = information[i]
# #     if dict_inf.get('license'):
# #         num_lic += 1
# for info in information:
#     if info.get('license'):
#         num_lic += 1

# print(num_lic)

# # Q2. 모든 사람의 나이 평균 구하기
# num_age = 0

# # for i in range(users_len):
#     # dict_inf = information[i]
#     # num_age += dict_inf.get('age')
# for info in information:
#     num_age += info.get('age')
# num_age_average = round(num_age / users_len,3)

# age_lst = [info['age'] for info in information]
# print(age_lst)
# print(num_age_average)

# # Q3. 라이센스가 없는 사람들의 이름 모으기
# list_nonlic = []

# # for i in range(users_len):
#     # dict_inf = information[i]
#     # a = dict_inf.get('name')
#     # b = dict_inf.get('license')
#     # if not b:
#         # list_nonlic.append(a)     
# for info in information:
#     a = info.get('name')
#     b = info.get('license')
#     if not b:
#         list_nonlic.append(a)
        
# name_lis = [info['name'] for info in information if not info.get('license')]
# print(name_lis)
# print(list_nonlic)


# ####
# users['information'].append({'name': 'ken', 'age' : 10, 'license' : True })
# users['total_user'] += 1
# print(users['total_user'])

# 모듈
# 카운트 다운이 있는 로또 번호 추첨기 만들기
import time
import random

for i in range(5):
    time.sleep(1)
    print(5-i)
a = [i+1 for i in range(45)]
number = random.sample(a,6)
number.sort()
print(number)

print(time.time())