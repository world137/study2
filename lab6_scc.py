from collections import defaultdict
   
#This class represents a directed graph using adjacency list representation
class Graph:
   
    def __init__(self,vertices):                    #O(2)
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
   
    # function to add an edge to graph
    def addEdge(self,u,v):                          #O(1)
        self.graph[u].append(v)
   
    # A function used by DFS
    def DFSUtil(self,v,visited):                    #O(n) recursive
        # Mark the current node as visited and print it
        visited[v]= True
        #print(v)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
  
  
    def fillOrder(self,v,visited, stack):           #O(n) recursive
        # Mark the current node as visited 
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # print("i = ",i)
            #print("graph v =",self.graph[v])
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
            
             
        stack = stack.append(v)
      
  
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):                        #O(n**2)
        g = Graph(self.V)
  
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
  
   
   
    # The main function that finds and prints all strongly
    # connected components
    def printSCCs(self):                            #O(n)?
        a = 1  
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        try:
            for i in range(self.V):
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)
        except IndexError :
            a = 0
  
        # Create a reversed graph
        gr = self.getTranspose()
           
         # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)
  
         # Now process all vertices in order defined by Stack
        try :
            while stack:
                i = stack.pop()
             
                if visited[i]==False:
                    gr.DFSUtil(i, visited)
        except IndexError : a = 0
        print(a)
# Create a graph given in the above diagram

#--------------------------------------------ส่วนรับอินพุต-----------------------------------------------------------------------------------

f = open('6.6.txt','r')
path = []
count = 0
while True :
    m = f.readline().split()
    #print('m =',len(m))
    if len(m) < 3 and len(path) != 0:               #เมื่อจบกราฟแรก
        g = Graph(len(path))
        for i in path:
            g.addEdge(int(i[0]),int(i[1]))
        g.printSCCs()
        
        path = []
        count = 0
        print('')    
    if len(m) < 3 :                                 #เมื่อขึ้นกราฟใหม่
        station = int(m[0])
        route = int(m[1])
        if station == 0 and route == 0:
            break
        print(station,route)
    #print(m)

    if len(m) == 3 :                                #เพิ่มpath
        start = m[0]
        stop = m[1]
        way = int(m[2])
        if  way == 1 :
            #print('type1')
            path.append([start,stop])
            print('path',count+1,'=',path[count])
            count+=1
        elif  way == 2 :
            #print('type2')
            path.append([start,stop])
            print('path',count+1,'=',path[count])
            count+=1
            path.append([stop,start])
            print('path',count+1,'=',path[count])
            count+=1