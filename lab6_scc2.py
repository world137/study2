# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:
    
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
        

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
        
	def DFSUtil(self,v,visited):
		# Mark the current node as visited and print it
		visited[v]= True
		print (v+1)
		#arr = arr + [v]
		#arr= []
		#arr += v

		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFSUtil(i,visited)
		#return arr
	# A function used by DFS



	def fillOrder(self,v,visited, stack):
		# Mark the current node as visited
		visited[v]= True
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.fillOrder(i, visited, stack)
		stack = stack.append(v)
	

	# Function that returns reverse (or transpose) of this graph
	def getTranspose(self):
		g = Graph(self.V)

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j,i)
		return g



	# The main function that finds and prints all strongly
	# connected components
	def printSCCs(self):
		
		stack = []
		# Mark all the vertices as not visited (For first DFS)
		visited =[False]*(self.V)
		# Fill vertices in stack according to their finishing
		# times
		for i in range(self.V):
			if visited[i]==False:
				self.fillOrder(i, visited, stack)

		# Create a reversed graph
		gr = self.getTranspose()
		
		# Mark all the vertices as not visited (For second DFS)
		visited =[False]*(self.V)

		# Now process all vertices in order defined by Stack
		count = 0        
		while stack:			
			arr = []
			i = stack.pop()
			if visited[i]==False:
				gr.DFSUtil(i, visited)
				print("")
				count += 1
		print("count components:",count)
		if count == 0:
			return 1
		else:
			return 0
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
# Create a graph given in the above diagram

    print('\nGraph',i+1,':')
    answer=g.printSCCs()
    ans.append(answer)
print(ans)
#This code is contributed by Neelam Yadav


# ทุกข้อน้อยกว่า 5 BF