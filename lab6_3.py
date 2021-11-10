# Algorithm 
def floyd(nV,G):
    #dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    dist=G
    vertex = []
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
        #for i in dist:
        #    print(i)
        #print('\n')
    # sol(nV,dist)
    return dist

# Printing the output
def sol(nV,dist):
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")



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
INF = 999
for i in range(len(lst)):
    cols = lst[i][0][0]
    metrix = [[INF]*cols for i in range(cols)]  
    for a in range(1,len(lst[i])):
        if lst[i][a][2] == 1:
            metrix[lst[i][a][0]-1][lst[i][a][1]-1] = 1
        elif lst[i][a][2] == 2:
            metrix[lst[i][a][0]-1][lst[i][a][1]-1] = 1
            metrix[lst[i][a][1]-1][lst[i][a][0]-1] = 1
    
    for m in range(cols):
        for n in range(cols):
            if m==n:
                metrix[m][n] = 0
    for k in metrix:
        print(k,)    
    print("\n") 
    # print('\nGraph',i+1,':')
    ansFloyd=floyd(cols,metrix)
    havePath=True
    for i in range(len(ansFloyd)):
        if INF in ansFloyd[i]:
            ans.append(0)
            havePath=False
            break
    if havePath:ans.append(1)
print('\nAnswer :',ans)