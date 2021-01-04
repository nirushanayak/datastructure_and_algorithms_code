from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited=[]
        self.queue=[]

    def add_connection(self,node1,node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def number_of_nodes(self,lev,V=1):
        level=0
        count=0
        self.visited.append(V)
        self.queue.append(V)
        self.queue.append('$')
        while  self.queue:
            V=self.queue.pop(0)
            if V=='$':
                level=level+1
                if (level==lev):
                    return count
                count=0
                if self.queue:
                    self.queue.append('$')
                continue
            print(self.graph[V])
            for i in self.graph[V]:
                if i not in self.visited:
                    self.visited.append(i)
                    self.queue.append(i)
                    count=count+1

graph=Graph()
num=int(input())
for i in range(num-1):
    node1,node2 = map(str,input().split())
    graph.add_connection(node1,node2)
level=int(input())
c=graph.number_of_nodes(2)
print(c)
