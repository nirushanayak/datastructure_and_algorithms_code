from _collections import defaultdict
import pprint

class Graph:
    def __init__(self,collections=[]):
        self.graph = defaultdict(list)
        self.collections=collections

    def add_edge(self,node1,node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)


    def shortest_path(self,vertices):
        distance = dict.fromkeys(['A','B','C','D','E','F'],-1)
        distance['A']=0
        q=[]
        path={}
        q.append('A')
        while q:
            u=q.pop(0)
            for v in self.graph[u]:
                if distance[v]==-1:
                    distance[v]=distance[u]+1
                    path[v]=u
                    q.append(v)
        print(distance)
        print(path)

Graph=Graph()
Graph.add_edge('A','B')
Graph.add_edge('A','C')
Graph.add_edge('B','D')
Graph.add_edge('B','E')
Graph.add_edge('C','F')
Graph.add_edge('E','F')
Graph.shortest_path(6)
