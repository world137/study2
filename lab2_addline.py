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

def permutationS(arr):
    lst=[]
    for i in range(len(arr)):
        lst.append(i)
    lst1=permutations(lst)
    lst2=[]
    for i in list(lst1):
        lst2.append(i) 
    return lst2

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



def h_path(arr):
    keep = []
    for i in range(len(arr)) :
        for j in range(len(arr[i])):
            a = Paths(i,j, arr)
            for k in range(len(a)) :
                if len(a[k]) == len(arr) :
                    keep.append(a[k])
    return keep

def h_cycle(arr) :
    lst = []
    keep = h_path(arr)
    for i in range(len(keep)):
        first = keep[i][0]
        last = keep[i][-1]
        if arr[first][last] == 1 :
            keep[i].append(first)
            lst.append(keep[i])

    return lst
                    

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


#arr=[[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
#print(permutationS(arr))
#print(len(permutationS(arr)))
#print('all',all_paths(arr))
arr=[[0 ,0 ,1, 1 ,0, 0 ,0 ,0],
 [0 ,0, 0, 1, 0, 0, 0, 0],
 [0, 0 ,0, 0, 0, 0, 0 ,0],
 [0, 0, 0, 0 ,0 ,0, 0 ,0],
 [0 ,0 ,0, 0, 0 ,0 ,1, 0],
 [0, 0 ,0, 0 ,0 ,0 ,1, 1],
 [0 ,0 ,0, 0, 0,0, 0, 0],
 [0 ,0, 0, 0 ,0, 0, 0, 0]]

ap=addLine(arr)
for w in ap:
    print(w)







