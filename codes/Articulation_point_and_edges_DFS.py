from collections import defaultdict
class Graph:

    def __init__(self,Num,Vertex):
        self.graph = defaultdict(list)
        self.dist={}
        self.low={}
        self.visited={}
        self.parent={}
        self.parent[Vertex]= None
        self.A_P=[]
        self.bridges=[]

    def add_connection(self,node1,node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def DFS_Articultion_point(self,time,Vertex):
        self.dist[Vertex]=self.low[Vertex]=time+1
        self.visited[Vertex]=True
        child=0
        for i in self.graph[Vertex]:
            if i not in self.visited:
                child=child+1
                self.parent[i]=Vertex
                self.DFS_Articultion_point(time+1,i)
                self.low[Vertex]=min(self.low[i],self.low[Vertex])
                if self.low[i]>self.dist[Vertex]:
                    self.bridges.append([Vertex,i])
                if self.parent[Vertex]==None and child>1:
                      self.A_P.append(Vertex)
                elif self.parent[Vertex]!=None and self.low[i]>= self.dist[Vertex]:
                    self.A_P.append(Vertex)
            elif i in self.parent and self.parent[Vertex]!=i:
                self.low[Vertex]=min(self.low[Vertex],self.dist[i])



n,m= input().split()
for i in range(1):
    node_1,node_2=input().split()
graph = Graph(n,node_1)
graph.add_connection(node_1,node_2)
for i in range(1,int(m)):
    node1,node2 = input().split()
    graph.add_connection(node1,node2)
graph.DFS_Articultion_point(0,node_1)
print(len(graph.A_P))
print(' '.join(map(str,sorted(graph.A_P))))
print(len(graph.bridges))
for i in sorted(graph.bridges):
    print(' '.join(map(str,i)))

