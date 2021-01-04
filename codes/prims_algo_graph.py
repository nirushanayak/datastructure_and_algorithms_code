from _collections import defaultdict
import heapdict
import sys
import pprint

class Graph:
    def __init__(self,collections=[]):
        self.graph = defaultdict(list)
        self.collections=collections

    def add_edge(self,node1,node2,val):
        n=[node2,val]
        self.graph[node1].append(n)
        n=[node1,val]
        self.graph[node2].append(n)

    def prims_algo(self,num):
        h=heapdict.heapdict()
        distance={}
        path={}
        for i in range(num):
            h[i]=sys.maxsize
            distance[i]=-1
        h[0]=0
        distance[0]=0
        while h:
            u,v= h.popitem()
            for vertex in self.graph[u]:
                new_distance= distance[u]+vertex[1]
                if distance[vertex[0]]==-1:
                    distance[vertex[0]] = vertex[1]
                    path[vertex[0]]= u
                    h[vertex[0]]=vertex[1]
                elif distance[vertex[0]]> new_distance:
                    distance[vertex[0]] = new_distance
                    path[vertex[0]] = u
                    h[vertex[0]] = new_distance
        print(distance)
        print(path)

graph=Graph()
graph.add_edge(0,1,1)
graph.add_edge(0,2,4)
graph.add_edge(0,3,3)
graph.add_edge(1,3,2)
graph.add_edge(2,3,5)
graph.prims_algo(4)

