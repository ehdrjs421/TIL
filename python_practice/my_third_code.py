# # 점수 관리
# # 김새싹 학생은 국어 시험에서 85점을, 영어 시험에서 90점을, 수학에서는 78 점을 맞았습니다.
# # (1) 위 데이터를 잘 관리할 수 있도록 딕셔너리 자료형을 만들어 보세요.
# # (2) 김새싹은 새로 시험 본 파이썬 과목에서 100점이라는 점수를 받았습니다. 앞서 생성한 딕셔너리에 추가해 주세요.
# # (3) 앞서 만든 딕셔너리를 사용하여 다음 형식으로 출력해 보세요

# dict = {'name':'김새싹','국어':85,'영어':90,'수학':78}

# dict['파이썬'] = 100

# for i in dict.keys():
#     if(i!='name'):
#         print(f"{i} 점수는 {dict[i]}점입니다")


# # 수강생 명단
# # 두 강좌의 수강생 명단이 집합으로 주어져 있습니다.
# python_class = {"철수","영희","민수"}
# data_class = {"영희","지현","민수"}
# # 아래를 각각 구하세요.
# # (1) 두 강좌를 모두 수강하는 학생
# # (2) 파이썬 강좌만 수강하는 학생
# # (3) 두 강좌 중 하나라도 수강한 학생

# print(python_class&data_class)
# #python_class.intersection(data_class)
# print(python_class - data_class)
# #python_class.difference(data_class)
# print(python_class | data_class)
# #python_class.union(data_class)


# 떡잎마을 반장선거
# # 후보가 없는 반장선거 
# # 표가 발생하면, 자동 입후보 되는 구조

votes = ['짱구','짱구','수지','짱구','훈이','맹구',
        '수지','수지','수지','짱구','유리','철수']
dict = {}
winner = []
for i in votes:
    if not (i in dict):
        dict[i] = 1
    else:
        dict[i] += 1
        
max_vote = max(dict.values())
for i,j in dict.items():
    if (j==max_vote):
        winner.append(i)
        
print(winner,max_vote)
        
# # 누가 반장이 될까요?