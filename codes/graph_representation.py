from collections import defaultdict
import pprint

class Graph:
    def __init__(self, collection=[]):
        self.graph = defaultdict(set)
        self.collection = collection

    def add_connections(self):
        for node1, node2 in self.collection:
            self.add(node1,node2)
            self.add(node2,node1)

    def add(self,node1,node2):
        self.graph[node1].add(node2)

    def remove_reference(self,node):
        for a,b in self.graph.items():
            try:
                b.remove(node)
            except:
                pass
        del self.graph[node]

def BFS(Graph,node):
    Queue = []
    visited = []
    Queue.append(node)
    visited.append(node)
    while (Queue):
        s=Queue.pop(0)
        print(s)
        for l in Graph[s]:
            if l not in visited:
                Queue.append(l)
                visited.append(l)

def shortest_path_unweight(Graph,node):
    L1=['A','B','C','D','E','F']
    Directions = dict.fromkeys(L1,-1)
    Queue=[]
    Directions[node]=0
    Queue.append(node)
    while(Queue):
        s=Queue.pop(0)
        for a in Graph[s]:
            if(Directions[a]==-1):
                Directions[a]=Directions[s]+1
                Queue.append(a)
    print(Directions)






connections = [('A', 'B'), ('A', 'C'), ('B', 'D'),
               ('B', 'E'), ('C', 'F'), ('E', 'F')]
G1 = Graph(connections)
G1.add_connections()
shortest_path_unweight(G1.graph,'A')
pretty_print = pprint.PrettyPrinter()
pretty_print.pprint(G1.graph)
# # G1.remove_reference('A')
# pretty_print = pprint.PrettyPrinter()
# pretty_print.pprint(G1.graph)
# BFS(G1.graph,'A')

# def main():
#     G1=Graph()
#     l1=list(map(int,input().split()))
#     for i in range(l1[1]):
#         l2=list(map(int,input().split()))
#         G1.add(l2[0],l2[1])
#     pretty_print = pprint.PrettyPrinter()
#     pretty_print.pprint(G1.graph)
#
#
# main()







