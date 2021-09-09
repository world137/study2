values = 0
arr=[[0,0,1,1,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,0],
     [0,0,0,0,0,0,1,1],
     [0,0,0,0,1,1,0,0],
     [0,0,0,0,0,1,0,0]]

# arr = [[1, 2 ,0, 2],
# [2, 1 ,2, 1],
# [0 ,2, 0, 2],
# [2, 1 ,2 ,1]]

# arr=[[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]

# arr = [[0, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
# [1 ,0 ,1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1, 1, 1],
# [1, 1 ,0, 1 ,1, 1, 1 ,1, 1 ,1 ,1 ,1 ,1 ,1, 1],
# [1 ,1, 1, 0, 1, 1 ,1 ,1 ,1, 1, 1 ,1 ,1 ,1, 1],
# [1 ,1, 1, 1 ,0 ,1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
# [1 ,1, 1, 1 ,1 ,0, 1 ,1 ,1 ,1 ,1, 1 ,1, 1 ,1],
# [1 ,1, 1, 1 ,1 ,1, 0 ,1 ,1, 1 ,1 ,1 ,1, 1 ,1],
# [1 ,1, 1, 1, 1 ,1, 1, 0, 1 ,1 ,1 ,1, 1, 1 ,1],
# [1 ,1, 1, 1 ,1, 1 ,1 ,1, 0, 1 ,1, 1, 1, 1, 1],
# [1 ,1 ,1, 1, 1 ,1, 1 ,1, 1, 0, 1, 1 ,1, 1, 1],
# [1 ,1, 1, 1, 1 ,1, 1 ,1, 1 ,1 ,0 ,1, 1, 1 ,1],
# [1 ,1, 1, 1, 1 ,1 ,1, 1, 1, 1 ,1 ,0 ,1 ,1 ,1],
# [1 ,1, 1, 1, 1 ,1 ,1 ,1, 1, 1, 1 ,1 ,0, 1, 1],
# [1 ,1 ,1, 1, 1 ,1, 1, 1 ,1, 1 ,1, 1, 1 ,0 ,1],
# [1, 1, 1, 1, 1, 1 ,1 ,1, 1 ,1 ,1 ,1, 1 ,1, 0]]

# while values <= 0 :
#     vertex = input("enter a number of vertexes : ")
#     if int(vertex) <= 0:
#         values = 0
#     else:
#         values = int(vertex)
#
# rows = int(vertex)
# cols = int(vertex)
# i = 0
# j = 0
# arr = [[0]*rows for i in range(cols)]
# arr2 = [[0]*rows for i in range(cols)]
# arr3 = [[0]*rows for i in range(cols)]
# value = ""
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         vector = input("enter vector " + str(i) + str(j) + " :")
#         if str(vector) == value:
#             print("error")
#             break
#         elif i == j :
#             arr[i][j] = 0
#             arr3[i][j] = int(vector)
#             if int(vector) != 0:
#                 print("Hamiltonian graph must not contain loops.")
#         elif i > j :
#             arr[i][j] = arr[j][i]
#             arr3[i][j] = arr3[j][i]
#             if int(vector) != 0 and int(vector) != 1:
#                 print("is not Hamiltonian graph")
#             elif arr[i][j] != int(vector) :
#                 print("is not Hamiltonian graph")
#         elif int(vector) == 0 or int(vector) == 1:
#             arr3[i][j] = int(vector)
#             arr[i][j] = int(vector)
#         else :
#             arr[i][j] = 1
#             arr3[i][j] = int(vector)
#             print("is not Hamiltonian graph")
#         arr2[i][j] = int(vector)
#     else:
#         continue
#     break
#
# for z in arr2:
#     print(z)
#
# print("\n")
# for x in arr3:
#     print(x)

from itertools import permutations

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
    print ('Add ',min(lst),' lines')
    return addLinePath


print("\n")
for l in arr:
    print(l)

def isHamiltonian(arr):
    is_H=True
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j and arr[i][j] != 0:
                is_H=False
            elif int(arr[i][j]) != 0 and int(arr[i][j]) != 1 :
                is_H=False
            elif arr[i][j] != arr[j][i]:
                is_H=False
    return is_H

def degree(arr) :
    keep = []
    for i in range(len(arr)):
        c = 0
        for j in range(len(arr[i])):
            c += arr[i][j]
            if j == len(arr[i]) - 1 :
                keep.append(c)
    print("degree in each vertex :" , keep)

def all_paths(arr):
    keep = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            a = Paths(i, j, arr)
            for k in range(len(a)):
                if len(a[k]) > 0:
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



def h_path(arr):
    # if isHamiltonian(arr):
        keep = []
        for i in range(len(arr)) :
            for j in range(len(arr[i])):
                a = Paths(i,j, arr)
                for k in range(len(a)) :
                    if len(a[k]) == len(arr) :
                        keep.append(a[k])
        return keep
    # else:
    #     return "Hamiltonian : False"

def h_cycle(arr) :
    # if isHamiltonian(arr):
        lst = []
        keep = h_path(arr)
        for i in range(len(keep)):
            first = keep[i][0]
            last = keep[i][-1]
            if arr[first][last] == 1 :
                keep[i].append(first)
                lst.append(keep[i])

        return lst
    # else:
    #     return "Hamiltonian : False"

print("\n")
degree(arr)

p = Paths(0,2,arr)
print("\n")
print("part :")
print("count part :",len(p))
for n in p:
    print(n)

hp = h_path(arr)
print("\n")
print("Hamiltonion path is : ")
print("count Hamiltonion path :" ,len(hp))
for l in hp:
    print(l)

hc = h_cycle(arr)
print("\n")
print("Hamiltonion cycle is : ")
print("count cycle :" ,len(hc))
for m in hc:
    print(m)

print("\n")
ap = addLine(arr)
for w in ap:
    print(w)
print("count :" ,len(ap))