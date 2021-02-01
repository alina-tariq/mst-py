class Graph:

    def __init__(self, numV):
        self.vertices = numV # num of vertices
        self.graph = [] # stores edges

    def addEdge(self, v1, v2, w):
        # adds new edge
        self.graph.append((v1, v2, w))

    def find(self, parent, vertex):
        # finds set for the given vertex
        if parent[vertex - 1] == vertex:
            return vertex
        return self.find(parent, parent[vertex - 1])

    def union(self, parent, rank, v1Set, v2Set):
        v1SetRoot = self.find(parent, v1Set) - 1
        v2SetRoot = self.find(parent, v2Set) - 1

        # adds smaller rank set to root of the
        # higher rank set and if they're equal arbitraily
        # attaches one set to root of the other set
        if rank[v1SetRoot] < rank[v2SetRoot]:
            parent[v1SetRoot] = v2SetRoot
        elif rank[v1SetRoot] > rank[v2SetRoot]:
            parent[v2SetRoot] = v1SetRoot
        else:
            parent[v2SetRoot] = v1SetRoot
            rank[v1SetRoot] += 1

    def minSpanTree(self):
        mSpanTree = []
        inputEdge = 0 # counter to go through all input edges
        mstEdge = 0 # counter to insert valid edges into MST
        maxEdge = self.vertices - 1 # max allowed edges in MST
        parent = []
        rank = []

        self.graph.sort(key=lambda tup: tup[2]) # sorts graph by weight

        for vertexNum in range(1, maxEdge + 2):
            parent.append(vertexNum)
            rank.append(0) # initializes rank

        while mstEdge < maxEdge:
            v1, v2, w = self.graph[inputEdge]
            inputEdge += 1

            # finds the set of both vertexes in the edge and if
            # they're not the same (aka they don't form a cycle)
            # appends the edge to the minimum spanning tree

            v1Set = self.find(parent, v1)
            v2Set = self.find(parent, v2)

            if v1Set != v2Set:
                mstEdge += 1
                mSpanTree.append((v1, v2, w))
                self.union(parent, rank, v1Set, v2Set) # used to detect cycle

        weight = sum(edge[2] for edge in mSpanTree)
        print(" ")
        print("Minimal Spanning Tree")
        print(" ")
        self.printGraph(mSpanTree)
        print(" ")
        print("The total weight of the spanning tree is", weight)

    def printGraph (self, minSpanTree=None):
        if (minSpanTree==None):
            minSpanTree = self.graph
        print("There are {0} vertices and {1} edges".format(self.vertices, len(minSpanTree)))
        print(" ")
        print("Vertices\tWeight")
        print(" ")
        for a in range(len(minSpanTree)):
            print("{0}\t{1}\t{2}".format(minSpanTree[a][0],minSpanTree[a][1],minSpanTree[a][2]))

#############################################

numVertices = input("Enter number of vertices: ")
numVertices = int(numVertices)
graph = Graph(numVertices)

print("Enter each edge in the following format: startvertex, endvertex, weight")
print("For example: 1, 2, 3")
print("Enter -1 to exit")

edge = input("Enter edge: ")

while (edge != "-1"):
    v1, v2, w = edge.split(',')
    v1 = int(v1)
    v2 = int(v2)
    w = int(w)
    graph.addEdge(v1, v2, w)
    edge = input("Enter edge: ")

print(" ")
print("Input Graph")
print(" ")
graph.printGraph()
graph.minSpanTree()
