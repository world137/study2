import itertools
from collections import defaultdict

def vertexCover1(graph,lstCover,k):
    lstCheck=[]
    for i in range(len(lstCover)):  #combination
        check=[0]*len(graph)
        notCover=False
        for m in range(len(graph)):
            for n in range(len(graph)):
                if graph[m][n]==1 and m not in lstCover[i] and n not in lstCover[i]:
                    notCover=True
            if notCover:
                break
        if (notCover==False):
            lstCheck.append(lstCover[i])
    return lstCheck

#O(n!/k!(n-k)! * (n^2)) k = จนจุด vertex cover / n = จนจุด


def result(lstRS):
    result=[]
    for i in range(len(lstRS)):
        lst=[]
        for j in range(len(lstRS[i])):
            lst.append(lstRS[i][j]+1)
        result.append(lst)
    return result

#-------------------------------------------------------------------------------------------------------

def VertexCover2(nv,graph):
    visited = [False] * (nv)
    for u in range(nv):
        if not visited[u]:
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    visited[u] = True
                    break
    result=[]
    for j in range(nv):
        if visited[j]:
            result.append(j+1)
    return result

#O(n^2) n = จน จุด

#-------------------------------------------------------------------------------------------------------

def vertexCover3(clause,nv):                  
    vertices=(len(nv)*2)+(len(clause)*3)        # จำนวนจุดของการฟ ==> nv = list
    cover=(len(nv))+(len(clause)*2)             # k
    graph = [[0]*vertices for i in range(vertices)]
    p=(len(nv)*2)                               #จุดเริ่มต้นของสามเหลี่ยมได้ล่าง
    for n in range(0,len(nv)):
        graph[n*2][n*2+1]=graph[n*2+1][n*2]=1   # กำหนดเส้นเชื่อมระหว่างจุด (ตัวแปร) ในเมทริกซ์ (จุดด้านบนสามเหลี่ยม) n = 0 ==> 0,1
    
    for i in range(len(clause)):
        graph[p][p+1]=graph[p+1][p]=1           # กำหนดเส้นเชื่อมระหว่างจุดในแต่ละสามเหลี่ยม ในเมทริกซ์
        graph[p][p+2]=graph[p+2][p]=1
        graph[p+1][p+2]=graph[p+2][p+1]=1

        for j in range(3):                      # 3-SAT
            v=(abs(clause[i][j])-1)*2           # หาตำแหน่งของค่าด้านบนที่ตรงกับค่าด้านล่างทีละจุด *2 คือ 1 ค่ามีทั้งบวกและลบ
            if clause[i][j]>0 :                 # กำหนดเส้นชื่อมระหว่างจุดตั้งต้นและสามเหลี่ยม ในเมทริกซ์            
                graph[p+j][v]=graph[v][p+j]=1
            else:
                graph[p+j][v+1]=graph[v+1][p+j]=1  # ค่าที่เช็คถ้าเป็นลบให้ +1 เป็นตำแหน่งถัดไป(ด้านบน)
        p+=3                                       # clause ถัดไป
    
    return (vertices,cover,graph)

#O(n+m) n = จน ตัวแปร , m = จน clause

#-------------------------------------------------------------------------------------------------------

f= open("1.3.txt", "r") 
inputLst = f.read().splitlines()
k = int(inputLst[0])
graph=[]
for i in range(1,len(inputLst)):
    graph.append([int(i) for i in inputLst[i].split()])
vertices=[int(i) for i in range(len(graph))]
test = list(itertools.combinations(vertices, k))

print("\nvertexCover - 1")
bf=vertexCover1(graph, test, k)
resultBF=result(bf)
if resultBF==[]:
    print("No")
else:
    print("Yes")
    for i in resultBF:
        print(i)

#-------------------------------------------------------------------------------------------------------

f= open("2.2.txt", "r") 
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
vc2 = VertexCover2(len(g),g)
print(vc2)
print(len(vc2))

#-------------------------------------------------------------------------------------------------------
    
# f= open("3.3.txt", "r") 
# inputLst = f.read().splitlines()
# m=int(inputLst[0])
# clause=[]
# for i in range(1,len(inputLst)):
#     clause.append([int(i) for i in inputLst[i].split()])
# vertices=[]
# for i in range(len(clause)):
#     for j in range(len(clause[i])):
#         if abs(clause[i][j]) not in vertices:
#             vertices.append(abs(clause[i][j]))

# result=vertexCover3(clause,vertices)
# print("\nvertexCover - 3")
# print(result[0])
# print(result[1])
# for i in result[2]:
#     text=''
#     for k in i:
#         text+=str(k)+' '
#     print(text)