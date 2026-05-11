INF = 9999999
count=0
v = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(v):
    row = list(map(int, input().split()))
    graph.append(row)

selected = [False] * v
selected[0] = True

edge_count = 0

print("\nEdge : Weight")

while edge_count < v - 1:
    minimum = INF
    x = 0
    y = 0

    for i in range(v):
        if selected[i]:
            for j in range(v):
                if (not selected[j]) and graph[i][j]:
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {graph[x][y]}")
    count+=graph[x][y]
    selected[y] = True
    edge_count += 1
print("Total weight :", count)

"""Title

Prim’s Minimum Spanning Tree (MST) Algorithm in Python

Objective

To find the Minimum Spanning Tree (MST) of a weighted graph using Prim’s Algorithm and display the selected edges with minimum cost.

Theory

Prim’s Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected weighted graph. A Minimum Spanning Tree is a set of edges that connects all vertices with the minimum possible total weight and without forming any cycle.

In this program, the graph is represented using an adjacency matrix. Each value in the matrix represents the weight between two vertices. A value of 0 means there is no direct edge between those vertices.

The algorithm starts from a selected vertex, here vertex 0, and gradually builds the spanning tree. It always selects the minimum-weight edge that connects a selected vertex to an unselected vertex.

A list called selected[] is used to keep track of vertices already included in the MST.

True means the vertex is selected.
False means the vertex is not selected yet.

Initially, only the first vertex is selected:

selected[0] = True

The algorithm repeatedly searches for the smallest edge connecting selected and unselected vertices. Once the minimum edge is found, that edge is added to the MST and the new vertex becomes selected.

This process continues until V - 1 edges are selected, where V is the number of vertices.

Prim’s Algorithm follows the greedy approach because at every step it chooses the smallest possible edge.

Important Points
Minimum Spanning Tree (MST)
Connects all vertices.
Uses minimum total cost.
Contains no cycles.
Prim’s Algorithm
Greedy algorithm for MST.
Starts from one vertex and expands the tree.
Weighted Graph
Graph edges contain weights.
Adjacency Matrix
Used to represent graph connections and weights.
Selected Array
Tracks vertices already included in MST.
Minimum Edge Selection
Smallest edge connecting selected and unselected vertex is chosen.
Edge Count
MST always contains V - 1 edges.
Greedy Method
Chooses locally minimum edge at every step.
No Cycles
Algorithm avoids forming cycles.

Applications
Network design
Road construction
Electrical wiring
Communication systems

Algorithm
Start the program.
Read number of vertices.
Input adjacency matrix.
Create selected array initialized as False.
Select first vertex.
Repeat until V - 1 edges are selected:
Find minimum edge between selected and unselected vertices.
Print selected edge and weight.
Mark new vertex as selected.
End the program.

Conclusion
This program implements Prim’s Algorithm to find the Minimum Spanning Tree of a weighted graph. It selects minimum-cost edges step by step and connects all vertices efficiently without forming cycles. The algorithm is widely used in real-world network and infrastructure design problems."""