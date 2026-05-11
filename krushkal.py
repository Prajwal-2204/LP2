class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y

        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):

        result = []

        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("\nEdges in Minimum Spanning Tree:")

        total_cost = 0

        for u, v, weight in result:
            total_cost += weight
            print(f"{u} - {v} : {weight}")

        print("Total Cost =", total_cost)


v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

g = Graph(v)

for i in range(e):
    u = int(input("Enter source vertex: "))
    v1 = int(input("Enter destination vertex: "))
    w = int(input("Enter weight: "))

    g.add_edge(u, v1, w)

g.kruskal_mst()

"""Title
Kruskal’s Minimum Spanning Tree (MST) Algorithm in Python

Objective
To find the Minimum Spanning Tree (MST) of a weighted graph using Kruskal’s Algorithm and calculate the minimum total cost.

Theory
Kruskal’s Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected weighted graph. A Minimum Spanning Tree is a subset of graph edges that connects all vertices with the minimum possible total weight and without forming any cycle.
In this program, the graph is represented using an edge list. Each edge contains:

Source vertex (u)

Destination vertex (v)

Weight (w)

The main idea of Kruskal’s Algorithm is:

Sort all edges according to increasing weight.

Select the edge with the smallest weight.

Add the edge if it does not create a cycle.

Repeat until all vertices are connected.

The program uses the Greedy Method because it always chooses the edge with the minimum weight at every step.
To detect cycles, the program uses the Disjoint Set (Union-Find) data structure. This structure helps in checking whether two vertices already belong to the same set or not.
The find() function is used to find the parent (root) of a vertex. If two vertices have the same parent, adding that edge would create a cycle.
The union() function combines two different sets into one set. Rank is used to keep the tree balanced and improve efficiency.
The algorithm continues selecting edges until the number of selected edges becomes V - 1, where V is the number of vertices.
Important Points


Minimum Spanning Tree (MST)

Connects all vertices.
Uses minimum total edge weight.
Contains no cycles.

Kruskal’s Algorithm

Greedy algorithm for MST.
Selects smallest edge first.

Weighted Graph
Graph edges contain weights/costs.


Edge Sorting
Edges are sorted in ascending order of weight.
Cycle Detection

Algorithm avoids cycles while adding edges.
Disjoint Set
Used for cycle checking.


Find Function
Finds parent/root of a vertex.
Union Function
Combines two sets.

Rank Array
Helps keep tree balanced.

Applications
Network design
Road construction
Cable connections
Electrical wiring


Algorithm
Start the program.
Read number of vertices and edges.
Input all graph edges with weights.
Store edges in graph list.
Sort edges in increasing order of weight.
Create parent and rank arrays.
Repeat until V - 1 edges are selected:
Select smallest edge.
Find parents of both vertices.
If parents are different:
Add edge to MST.
Perform union operation.
Print MST edges.
Calculate and print total cost.
End the program.


Conclusion
This program implements Kruskal’s Algorithm to find the Minimum Spanning Tree of a weighted graph. It uses the greedy approach to select minimum-cost edges and the Union-Find method to avoid cycles. The algorithm efficiently finds the minimum total cost required to connect all vertices in the graph."""