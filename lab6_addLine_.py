from itertools import product,combinations
from collections import defaultdict
import copy

class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
        
	def addEdge(self,u,v):
		self.graph[u].append(v)
        
	def DFSUtil(self,v,visited,arr=[]):
		visited[v]= True
		#print (v+1, end=' ')
		arr+=[v+1]
		for i in self.graph[v]:
			if visited[i]==False:
				dfs=self.DFSUtil(i,visited,arr)
		#print('arr',arr)
		return arr

	def fillOrder(self,v,visited, stack):
		visited[v]= True
		for i in self.graph[v]:
			if visited[i]==False:
				self.fillOrder(i, visited, stack)
		stack = stack.append(v)
	
	def getTranspose(self):
		g = Graph(self.V)
		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j,i)
		return g

	def printSCCs(self):
		stack = []
		visited =[False]*(self.V)
		for i in range(self.V):
			if visited[i]==False:
				self.fillOrder(i, visited, stack)

		gr = self.getTranspose()
		visited =[False]*(self.V)    
		components=[]  
		while stack:			
			i = stack.pop()
			if visited[i]==False:
				dfs=gr.DFSUtil(i, visited,arr=[])
				components.append(dfs)
		return components

#สร้างกราฟใหม่ 1component คือ 1จุด
def newG(lst,g):
	matrix = [[0]*len(g) for i in range(len(g))]
	line=list(combinations(g, 2))
	for n in range(len(line)): 
		vertice=list(product(line[n][0][:-1],line[n][1][:-1]))
		for i in range(len(vertice)):  #จับคู่

			if [vertice[i][0],vertice[i][1],1] in lst:
				matrix[line[n][0][-1][0]][line[n][1][-1][0]] = 1

			elif [vertice[i][0],vertice[i][1],2] in lst:
				matrix[line[n][0][-1][0]][line[n][1][-1][0]] = 1
				matrix[line[n][1][-1][0]][line[n][0][-1][0]] = 1

			elif [vertice[i][1],vertice[i][0],1] in lst:
				matrix[line[n][1][-1][0]][line[n][0][-1][0]] = 1

			elif [vertice[i][1],vertice[i][0],2] in lst:
				matrix[line[n][0][-1][0]][line[n][1][-1][0]] = 1
				matrix[line[n][1][-1][0]][line[n][0][-1][0]] = 1
	return matrix

#BF ไล่เติมที่ละ 1 เส้น , 2 เส้น ... ไปเรื่อยๆ แล้วเช็คจนไปได้ทุกทาง
def addLine(g):
	vertices=[]
	for i in range(len(g)):
		for j in range(len(g)):
			if g[i][j]==0 and (j,i) not in vertices and i!=j:
				vertices.append([i,j])

	for n in range(1,len(g)):
		line=list(combinations(vertices, n))
		for i in range(len(line)):
			newG = copy.deepcopy(g)
			for j in range(len(line[i])):
				newG[line[i][j][0]][line[i][j][1]]=1
				newG[line[i][j][1]][line[i][j][0]]=1
			gSCC = Graph(len(newG))
			for a in range(len(newG)):
				for b in range(len(newG)):
					if newG[a][b]==1:
						gSCC.addEdge(a,b)
			scc=gSCC.printSCCs()
			#Done=False
			if len(scc) == 1:
				print('Add',n,'line')
				return

inputLst="""8 15
1 5 1
1 6 2
2 1 1
2 4 1
3 4 1
3 5 2
3 8 1
5 2 1
5 4 1
5 7 1
6 7 1
7 1 1
7 2 1
7 8 1
8 4 1
20 35
1 4 1
2 1 1
3 2 1
3 5 1
3 7 1
3 9 1
4 3 1
4 5 1
5 2 1
5 6 1
6 1 1
6 2 1
6 3 1
7 8 1
8 9 1
9 7 1
10 13 1
11 10 1
12 15 1
13 12 1
13 14 2
13 20 1
14 11 1
14 12 1
14 15 2
15 10 1
15 11 1
16 19 1
17 16 1
18 16 1
18 17 1
19 18 1
20 5 1
20 15 1
20 19 1
9 7
1 2 2
2 3 2
3 4 2
3 6 2
4 5 2
7 8 2
8 9 2
16 16
2 1 1
3 2 1
4 1 1
4 3 1
5 6 1
5 7 1
6 7 1
8 9 2
9 10 2
10 11 1
11 12 1
12 13 1
13 14 1
14 15 1
15 16 1
16 11 1
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
    g = Graph(cols)
    for a in range(1,len(lst[i])):
        if lst[i][a][2] == 1:
            g.addEdge(lst[i][a][0]-1, lst[i][a][1]-1)
        elif lst[i][a][2] == 2:
            g.addEdge(lst[i][a][0]-1, lst[i][a][1]-1)
            g.addEdge(lst[i][a][1]-1, lst[i][a][0]-1)
    print('\nGraph',i+1,':')
    scc=g.printSCCs()
    print(scc)
    for m in range(len(scc)):
        scc[m].append([m]) # ตั้งชื่อจุดใหม่
    print("count components:",len(scc))
    if len(scc) == 1:
    	ans.append(1)
    else:
    	ans.append(0)
    	addLine(newG(lst[i], scc))
    	
print('\nAnswer :',ans)




