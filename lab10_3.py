
from collections import defaultdict

def VertexCover2(nv,graph,matrix):
    visited = [False] * (nv)
    d = {}
    max_len = 0
    isCover = False
    while(isCover == False):
        for i in range(len(graph)):
            if(max_len < len(graph[i])):
                max_len = i
        for j in range(len(matrix)):
            matrix[max_len][j] = 0
            matrix[j][max_len] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    break
                elif(i == len(matrix) and j == len(matrix)):
                    isCover = True
    print(matrix)
    print(graph)
    print(max_len)
    print(graph[max_len])

    

            
    # for u in range(nv-1,-1,-1):
    #     if not visited[u]:
    #         for v in graph[u]:
    #             if not visited[v]:
    #                 visited[v] = True
    #                 visited[u] = True
    #                 break
    result=[]
    for j in range(nv):
        if visited[j]:
            result.append(j+1)
    return result


f= open("10_2.txt", "r") 
inputLst = f.read().splitlines()
graph=[]
for i in range(len(inputLst)):
    graph.append([int(i) for i in inputLst[i].split()])
g = defaultdict(list)
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j]==1:
            g[i].append(j)

print("\nvertexCover - 2")
# print(g)
# vc2 = VertexCover2(len(g),g)
# print(vc2)
# print(len(vc2))
VertexCover2(len(g),g,graph)