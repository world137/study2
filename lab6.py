from itertools import combinations
def Paths(u, v, arr, path=[]):
    uPath = arr[u]
    path = path + [u]

    if u >= len(arr) or v >= len(arr): # จุดเกิน
        return []
    if u == v: # u ไปถึงปลายทาง
        return [path]
    paths = []

    for node in range(0, len(uPath)): # วนลูปในแต่ละแถวของ arr
        if uPath[node] == 1: #ตำแหน่งที่ node ใน uPath เป็น 1 คือมีเส้นเชื่อมระหว่างจุด
            if node not in path: # ถ้า node นั้นไม่เคยอยู่ใน path = ไม่เคยผ่านจุดนั้นมาก่อน ให้ใส่ใน path แล้ววนหาตัวถัดไปโดยใช้ subpaths
                subpaths = Paths(node, v, arr, path) # u เปลี่ยนค่าเป็น node
                for subpath in subpaths:
                    paths.append(subpath)
    return paths
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

# inputLst="""5 10 
# 1 2 1 
# 1 3 1 
# 1 5 1 
# 2 3 2
# 2 4 1
# 3 4 1
# 3 5 1
# 4 1 1
# 4 5 1
# 5 2 1
# 4 4
# 1 2 1
# 2 4 1
# 3 4 1
# 4 1 1
# 4 5
# 1 2 2
# 2 3 1
# 2 4 1
# 3 1 1
# 3 4 2
# 0 0""".splitlines()


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
4 5
1 2 1
1 1 1
2 1 1
3 4 1
2 4 2
2 1
1 2 2
4 5
1 2 1
1 1 1
2 1 1
3 4 1
2 4 2
2 1
1 2 2
4 5
1 2 1
1 1 1
2 1 1
3 4 1
2 4 2
2 1
1 2 2
4 5
1 2 1
1 1 1
2 1 1
3 4 1
2 4 2
2 1
1 2 2
4 5
1 2 1
1 1 1
2 1 1
3 4 1
2 4 2
2 1
1 2 2
4 5
1 2 1
1 1 1
2 1 1
3 4 1
2 4 2
2 1
1 2 2
4 5
1 2 1
1 1 1
2 1 1
3 4 1
2 4 2
2 1
1 2 2
3 3
1 2 1
2 3 1
3 1 1
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

ans=[]
for i in range(len(lst)):
    cols = lst[i][0][0] # วนหาตัวแรกของแต่ละ graph ==> ดูจำนวนจุด
    matrix = [[0]*cols for i in range(cols)]  # สร้าง matrix เท่ากับจำนวนจุด
    for a in range(1,len(lst[i])):
        if lst[i][a][2] == 1:
            matrix[lst[i][a][0]-1][lst[i][a][1]-1] = 1
        elif lst[i][a][2] == 2:
            matrix[lst[i][a][0]-1][lst[i][a][1]-1] = 1
            matrix[lst[i][a][1]-1][lst[i][a][0]-1] = 1 # กำหนดค่าให้กับ matrix (-1 matrix เริ่มที่ 1)
    numCity=[] # list จุดทั้งหมด
    for j in range(lst[i][0][0]):
        numCity.append(j+1)
    allCity=list(combinations(numCity,2)) # [[1,2][1,3][2,3]]
    havePath=True
    for k in range(len(allCity)):
        path1 = Paths(allCity[k][0]-1,allCity[k][1]-1,matrix) #ขาไป
        path2 = Paths(allCity[k][1]-1,allCity[k][0]-1,matrix) #ขากลับ
        if len(path1)==0 or len(path2)==0:
            ans.append(0)
            havePath=False
            break
    if havePath:ans.append(1)
print(ans)