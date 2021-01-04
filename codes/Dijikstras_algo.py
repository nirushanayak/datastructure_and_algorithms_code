from _collections import defaultdict
import heapdict
import  pprint
import sys

class Graph:
    def __init__(self, v, collection=[]):
        self.graph = defaultdict(list)
        self.collection = collection
        self.v=v

    def add_connections(self):
        for node1, node2 in self.collection:
            self.add(node1,node2)
            self.add(node2,node1)

    def addEdge(self,node1,node2,val):
        node=[node2,val]
        self.graph[node1].append(node)

        node=[node1,val]
        self.graph[node2].append(node)

    def remove_reference(self,node):
        for a,b in self.graph.items():
            try:
                b.remove(node)
            except:
                pass
        del self.graph[node]

    def dijikstras(self,Vertex):
        h = heapdict.heapdict()
        distance={}
        path={}
        path[0]=None
        for i in range(self.v):
            distance[i]=sys.maxsize
            h[i]=sys.maxsize
        # print(distance)
        h[0]=0
        distance[0]=0
        print(list(h.items()))
        while h:
            u,temp = h.popitem()
            for node in self.graph[u]:
                vertex = node[0]
                if vertex in h and distance[u]!=sys.maxsize and node[1]+distance[u]<distance[vertex]:
                    distance[vertex]= node[1]+distance[u]
                    h[vertex]=distance[vertex]
                    path[vertex]=u
        print(distance)
        print(path)
        print(list(h.items()))






graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijikstras(0)
# prettyprint= pprint.PrettyPrinter()
# prettyprint.pprint(Graph.graph)

