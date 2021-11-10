from itertools import permutations


def all_paths(arr):
    keep = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            a = Paths(i, j, arr)
            for k in range(len(a)):
                if len(a[k]) > 1:
                    keep.append(a[k])
    return keep
                    
def Paths(u, v, arr, path=[]):
    a = []
    if arr == a:
        return print("error")

    uPath = arr[u] #เลือกทีละแถวของ arr
    path = path + [u] # เก็บจุด u ลง path

    if u >= len(arr) or v >= len(arr): # กำหนดจุดนอกเหนือจุดที่มี
        return []
    if u == v: # จุดเริ่มต้นวิ่งไปจนกลายเป็นจุดสุดท้าย
        return [path]
    paths = []

    for node in range(0, len(uPath)): # วนลูปในแต่ละแถวของ arr
        if uPath[node] == 1: #ตำแหน่งที่ node ใน uPath เป็น 1 คือมีเส้นเชื่อมระหว่างจุด
            if node not in path: # ถ้า node นั้นไม่เคยอยู่ใน path = ไม่เคยผ่านจุดนั้นมาก่อน ให้ใส่ใน path แล้ววนหาตัวถัดไปโดยใช้ subpaths
                subpaths = Paths(node, v, arr, path) # u เปลี่ยนค่าเป็น node
                for subpath in subpaths:
                    paths.append(subpath)
    return paths

def permutationS(arr):
    lst=[]
    for i in range(len(arr)):
        lst.append(i)
    lst1=permutations(lst)
    lst2=[]
    for i in list(lst1):
        lst2.append(i) 
    return lst2

def addLine(arr):
    a_path=all_paths(arr)
    a_per=permutationS(arr)
    lst=[]
    for i in range(len(a_per)) :
        cnt=0
        for j in range(len(a_per[i])-1):
            first=a_per[i][j]
            second=a_per[i][j+1]
            node=[first,second]
            if node not in a_path:
                cnt+=1
        lst.append(cnt)
    addLinePath=[]
    for i in range(len(a_per)):
        if lst[i]==min(lst):
            addLinePath.append(a_per[i])
    print ('Add ',min(lst),' line')
    return addLinePath

def floyd(nV,dist,Path):
    for r in range(nV): # จุดแวะพัก
        for p in range(nV): # จุดเริ่มต้น
            for q in range(nV): # จุดปลายทาง
                if dist[p][q] > dist[p][r] + dist[r][q]: # ทางใหม่น้อยกว่าจุดเดิมมั้ย
                    dist[p][q] = dist[p][r] + dist[r][q] # อัพเดทเส้นทางใหม่
                    Path[p][q]=Path[p][r]+Path[r][q]

    #     for i in Path:
    #        print(i)
    #     for i in dist:
    #        print(i)
    #     print('\n')
    # sol(nV,dist)
    # for i in Path:
    #     print(i)
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


inputLst="""6 6
1 2 1
2 3 1
4 3 1
4 5 1
5 6 1
6 2 1
3 2
1 2 1
2 3 2
10 17
1 3 1
1 5 1
1 6 1
2 5 1
2 6 1
3 4 1
5 6 1
7 4 1
8 1 1
8 4 1
9 2 1
9 6 1
9 10 2
10 3 1
10 6 1
10 7 1
10 8 1
16 29
1 6 2
2 1 1
2 3 1
2 7 1
2 8 1
3 4 1
3 7 1
3 10 1
3 14 1
4 5 2
4 6 1
4 9 1
5 7 1
6 9 2
6 15 1
7 6 1
7 13 1
8 3 1
8 7 1
8 9 2
9 2 1
9 5 1
9 10 1
10 5 1
11 7 1
12 3 1
12 4 1
13 9 1
16 10 1
0 0""".splitlines()

lst=[]
for i in range(len(inputLst)):
    if inputLst[i]=='0 0': break
    else:  
        strInput=[int(i) for i in inputLst[i].split()]
        if len (strInput)==2:
            lst.append([strInput]) # เจอกราฟใหม่ใส่ลงใน array
        else:
            lst[len(lst)-1].append(strInput) # กราฟเดิมเก็บลงใน graph [[graph1][graph2]]

INF = 999
ans=[]
for i in range(len(lst)):
    cols = lst[i][0][0] # วนหาตัวแรกของแต่ละ graph ==> ดูจำนวนจุด
    Graph = [[INF]*cols for i in range(cols)]  # สร้าง matrix เท่ากับจำนวนจุด
    matrix = [[0]*cols for i in range(cols)]
    Path = [[None]*cols for i in range(cols)]
    for a in range(1,len(lst[i])):
        if lst[i][a][2] == 1:
            Graph[lst[i][a][0]-1][lst[i][a][1]-1] = 1
            matrix[lst[i][a][0]-1][lst[i][a][1]-1] = 1
            Path[lst[i][a][0]-1][lst[i][a][1]-1] = [lst[i][a][0]] # กำหนด path เริ่มต้น
        elif lst[i][a][2] == 2:
            Graph[lst[i][a][0]-1][lst[i][a][1]-1] = 1
            Graph[lst[i][a][1]-1][lst[i][a][0]-1] = 1 # กำหนดค่าให้กับ matrix (-1 matrix เริ่มที่ 1)

            matrix[lst[i][a][0]-1][lst[i][a][1]-1] = 1
            matrix[lst[i][a][1]-1][lst[i][a][0]-1] = 1 

            Path[lst[i][a][0]-1][lst[i][a][1]-1] = [lst[i][a][0]]
            Path[lst[i][a][1]-1][lst[i][a][0]-1] = [lst[i][a][1]] 

    #for i in Path:
    #        print(i)
    for m in range(cols):
        for n in range(cols):
            if m==n:
                Graph[m][n] = 0
    
    newGraph = addLine(matrix)
    for w in newGraph:
        print(w)

    print('\nGraph',i+1,':')
    # for i in matrix:
    #         print(i)
    # print('\n')
    ansFloyd=floyd(cols,Graph,Path)
    havePath=True
    for i in range(len(ansFloyd)):
        if INF in ansFloyd[i]:
            ans.append(0)
            havePath=False
            break
    if havePath:ans.append(1)
print('\nAnswer :',ans)