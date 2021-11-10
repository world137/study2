


def floyd(nV,matrix,Path):
    for r in range(nV): # จุดแวะพัก
        for p in range(nV): # จุดเริ่มต้น
            for q in range(nV): # จุดปลายทาง
                if matrix[p][q] > max(matrix[p][r], matrix[r][q]): # ทางใหม่เบากว่าจุดเดิมมั้ย
                    matrix[p][q] = max(matrix[p][r], matrix[r][q]) # อัพเดทเส้นทางใหม่
                    Path[p][q]=Path[p][r]+Path[r][q]

    return 

inputLst="""7 9 3
1 2 50
1 3 60
2 4 120
2 5 90
3 6 50
4 6 80
4 7 70
5 7 40
6 7 140
1 7
2 6
6 2""".splitlines()
lst = []
for i in range(len(inputLst)):
    strInput=[int(i) for i in inputLst[i].split()]
    lst.append(strInput)
vertices=lst[0][0] 
edge=lst[1:lst[0][1]+1]
find=lst[lst[0][1]+1:]

INF = 999
matrix = [[INF]*vertices for i in range(vertices)]
path = [[None]*vertices for i in range(vertices)]

for j in range(len(edge)):
    matrix[edge[j][0]-1][edge[j][1]-1] = edge[j][2]
    matrix[edge[j][1]-1][edge[j][0]-1] = edge[j][2]
    path[edge[j][0]-1][edge[j][1]-1] = edge[j][0]
    path[edge[j][1]-1][edge[j][0]-1] = edge[j][1]
for l in range(len(matrix)):
    matrix[l][l] = 0

floyd(vertices,matrix,path)

for n in range(len(find)):
    a = matrix[find[n][0]-1][find[n][1]-1]
    if(a == INF):
        print(find[n],"no path")
    else:
        print(find[n],"ans :",a)
        print('path :',Path[find[n][0]-1][find[n][1]-1]+[find[n][1]])
        