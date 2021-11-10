import sys
def minDistance(V, dist, sptSet):
    min = sys.maxsize
    zero=True
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v
            zero=False
    if zero:min_index = 'error'
    return min_index

def dijkstra(V, graph, src):
    dist = [sys.maxsize] * V
    sptSet = [False] * V
    dist[src] = 0
    for i in range(V):
        u = minDistance(V, dist, sptSet)
        if u == 'error' : 
            dist = [0] * V
            break
        else:
            sptSet[u] = True
            for v in range(V):
                if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]       
    return dist
'''
inputLst="""4 5
1 2 1
1 3 2
2 4 1
3 4 1
4 1 2
3 2
1 2 2
1 3 2
3 2
1 2 2
1 3 1
0 0""".splitlines()
'''
inputLst="""5 10
1 2 1
1 3 1
1 4 1
1 5 2
2 3 1
2 4 1
2 5 1
3 4 1
3 5 1
4 5 1
4 5 
1 2 1
1 3 2
2 3 1
3 4 1
4 2 1
5 5
1 2 1
1 5 1
2 4 1
3 1 1
4 3 1
17 18
1 2 2
2 3 2
3 4 2
4 5 2
5 6 1
6 7 1
6 9 1
7 8 1
8 10 1
9 10 1
10 11 1
11 12 1
11 13 2
12 5 1
13 14 2
13 16 2
14 15 2
16 17 2
0 0""".splitlines()

lst=[]
for i in range(len(inputLst)):
    if inputLst[i]=='0 0': break
    else:  
        strInput=[int(i) for i in inputLst[i].split()]
        if len (strInput)==2:
            lst.append([strInput])
        else:
            lst[len(lst)-1].append(strInput)
            
ans=[]
for i in range(len(lst)):
    cols = lst[i][0][0]
    metrix = [[0]*cols for i in range(cols)]  
    for a in range(1,len(lst[i])):
        if lst[i][a][2] == 1:
            metrix[lst[i][a][0]-1][lst[i][a][1]-1] = 1
        elif lst[i][a][2] == 2:
            metrix[lst[i][a][0]-1][lst[i][a][1]-1] = 1
            metrix[lst[i][a][1]-1][lst[i][a][0]-1] = 1
            
    havePath=True
    for m in range(lst[i][0][0]):
        D = dijkstra(lst[i][0][0],metrix,m)
        if D==[0]*cols:
            ans.append(0)
            havePath=False
            break
    if havePath:ans.append(1)
print(ans)