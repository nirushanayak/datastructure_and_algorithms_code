from collections import defaultdict
class Graph:

    def __init__(self,Num,Vertex):
        self.graph = defaultdict(list)
        self.visited=[]
        self.stck=[]

    def add_connection(self,node1,node2):
        self.graph[node1].append(node2)

    def dfs(self,Vertex):
        self.visited.append(Vertex)
        for i in self.graph[Vertex]:
            if i  not in self.visited:
                self.dfs(i)
        self.stck.insert(0,Vertex)





n,m= input().split()
for i in range(1):
    node_1,node_2=input().split()
graph = Graph(n,node_1)
graph.add_connection(node_1,node_2)
for i in range(1,int(m)):
    node1,node2 = input().split()
    graph.add_connection(node1,node2)
graph.dfs(node_1)
print(' '.join(map(str,graph.stck)))

