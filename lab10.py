from itertools import combinations
def vertex_cover(k,matrix):
    lst = [0] * len(matrix)
    c = 0
    for i in range(len(lst)):
        lst[i] = c
        c += 1
    
    com = combinations(lst,k)
    lst_ans = []
    for j in list(com):
        ans = check(j,matrix)
        if(ans != []):
            lst_ans.append(ans)
    
    if(len(lst_ans) != 0):
        print("Yes")
        for l in lst_ans:
            print(l)
    else:
        print("No")
              
def check(vertex,matrix):
    s = set()
    new_s = set()
    zero = []
    for i in range(len(vertex)):
        s.add(vertex[i])
        new_s.add(vertex[i])      
    
    for k in s:  
        # print("s",s,k)    
        for j in range(len(matrix)):
            # print("matrix[k][j]" , matrix[k][j])
            if(matrix[k][j] == "1"):
                # print(k,j,"matrix",matrix[k][j])
                new_s.add(j)

    print("new",new_s)
    if(len(new_s) == len(matrix)):
        # print("vertex",vertex)
        return(vertex)
    else:
        return(zero)

def approximation(matrix):
    lst = [0] * len(matrix)
    c = 0
    for i in range(len(lst)):
        lst[i] = c
        c += 1
    
    arr = []
    i = 1
    while(i <= len(matrix)):
        com = combinations(lst,i)
        for j in range(len(matrix)):
            for k in com:
                print(k)
                s = set()
                for l in range(len(k)):
                    print(k[l])
                    s.add(l)
                    if(matrix[j][l] == "1" or matrix[l][j] == "1"):
                        s.add(j)
        arr.append(s)
        i += 1
    print(arr)   
        
with open("10.txt", "r") as file:
    inputLst = file.read().splitlines()


k = inputLst[0]
k = int(k)
matrix = []
i = 1
while(i < len(inputLst)):
    lst = inputLst[i].split(' ')
    matrix.append(lst)
    i += 1

vertex_cover(k,matrix)
approximation(matrix)