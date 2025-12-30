# a = "word"
# b = str(4)
# c = a + " is " + b
# print(c)

# #/////////////////
# #소수 판별시 사용
# for i in (2):
#         check = 0
#         for j in range(2,int(i**(1/2))+1):
#             if(i % j == 0):
#                 check = 1 
#                 break
#         if (check == 0):
#             answer += 1
#             print(i)

# # 딕셔너리 기능확인  
# a = {}
# print(len(a))
# for i in range(2):
#     a[i] = 3
# for i in range(2):
#     for j in a:
#         if (i == j):
#             a[i] -= i
# print(a)
# print(len(a))

# # 리스트 기능 확인
# a =[1,3,2,4]
# print(min(a))

# # for 문 기능 확인
# for i in range(3):
#     if i == 1:
#         continue
#     print(i)

# 재귀함수 테스트
# def solution(n, edges):
    # answer = 1
    # check = {1}
    # for i in range(len(edges)):
    #     if (edges[i][0]<edges[i][1]):
    #         if(edges[i][0] in check):
    #             if (answer < edges[i][1]):
    #                 answer = edges[i][1]
    #             check.add(edges[i][1])
    #     else:
    #         if(edges[i][1] in check):
    #             if (answer < edges[i][0]):
    #                 answer = edges[i][0]
    #             check.add(edges[i][0])

    # print(check)
    # return answer

# edges = [[0,1],[2,3],[4,2],[3,4]]
# edges = [sorted(edge) for edge in edges]
# # x.sort(key=lambda x: (x[0], x[1]))
# print(edges)


# def solution(n, edges):
#     # 인접 리스트 생성
#     graph = [[] for _ in range(n + 1)]
#     for a, b in edges:
#         graph[a].append(b)
#         graph[b].append(a)

#     visited = [False] * (n + 1)

#     # 재귀 DFS
#     def dfs(node):
#         visited[node] = True
#         count = 1  # 현재 정점 포함

#         for next_node in graph[node]:
#             if not visited[next_node]:
#                 count += dfs(next_node)

#         return count

#     # 1번 정점부터 탐색 시작
#     return dfs(1)

# def solution(n, edges):
#     reachable = {1}   # 1번에서 도달 가능하다고 '가정'된 집합
#     changed = True

#     while changed:
#         changed = False
#         for a, b in edges:
#             if a in reachable and b not in reachable:
#                 reachable.add(b)
#                 changed = True
#             elif b in reachable and a not in reachable:
#                 reachable.add(a)
#                 changed = True

#     return len(reachable)


a = [[-5,2],[2,1],[3,-6]]
a.sort(key = lambda x : (-(x[0]+x[1]),-x[0]))
print(a)

b = [1,3]
b.append(2)
print(b.index(3))
print(b)