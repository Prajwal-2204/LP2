# Single Source Shortest Path using Dijkstra Algorithm

v = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(v):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex: "))

visited = [False] * v
distance = [float('inf')] * v

distance[source] = 0

for _ in range(v):

    min_distance = float('inf')
    u = -1

    # Find minimum distance vertex
    for i in range(v):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            u = i

    visited[u] = True

    # Update distances
    for j in range(v):

        if graph[u][j] > 0 and not visited[j]:

            if distance[u] + graph[u][j] < distance[j]:

                distance[j] = distance[u] + graph[u][j]

print("\nShortest Distances from Source Vertex", source)

for i in range(v):
    print("Vertex", i, "=", distance[i])


    """Title

Single Source Shortest Path Using Dijkstra Algorithm in Python

Objective

To find the shortest distance from one source vertex to all other vertices in a weighted graph using Dijkstra’s Algorithm.

Theory

Dijkstra’s Algorithm is a graph traversal algorithm used to find the shortest path from a single source vertex to all other vertices in a weighted graph. The algorithm works only when all edge weights are non-negative.

In this program, the graph is represented using an adjacency matrix. Each element of the matrix represents the weight between two vertices. If the value is 0, it means there is no direct connection between those vertices.

The algorithm starts from the source vertex entered by the user. Initially, the distance of all vertices is set to infinity using:

distance = [float('inf')] * v

This means the shortest path is unknown at the beginning. The source vertex distance is set to 0 because the distance from the source to itself is always zero.

A visited[] array is used to keep track of vertices that are already processed. The algorithm repeatedly selects the unvisited vertex having the minimum distance value. After selecting that vertex, the algorithm checks all its neighboring vertices and updates their distances if a shorter path is found.

The update condition is:

if distance[u] + graph[u][j] < distance[j]

This means:

Current shortest path to vertex j
is compared with
new path through vertex u

If the new path is shorter, the distance is updated.

The process continues until all vertices are visited. Finally, the program prints the shortest distance from the source vertex to every other vertex.

Important Points
Dijkstra Algorithm
Finds shortest path from one source vertex.
Weighted Graph
Graph edges contain weights/costs.
Adjacency Matrix
Represents graph connections and weights.
Source Vertex
Starting point of shortest path calculation.
Distance Array
Stores shortest distances from source.
Visited Array
Tracks processed vertices.
Infinity Value
Used to represent unknown large distance.
Minimum Distance Selection
Algorithm selects nearest unvisited vertex.
Distance Update
Updates shorter path if found.
Greedy Algorithm
Chooses locally shortest path step by step.
Applications
GPS navigation
Network routing
Maps and path finding

Algorithm
Start the program.
Read number of vertices.
Input adjacency matrix.
Read source vertex.
Create visited[] array initialized as False.
Create distance[] array initialized as infinity.
Set source distance as 0.
Repeat for all vertices:
Find unvisited vertex with minimum distance.
Mark it as visited.
Check all adjacent vertices.
Update distances if shorter path exists.
Print shortest distances from source vertex.
End the program.

Conclusion
This program implements Dijkstra’s Algorithm to find the shortest distance from a single source vertex to all other vertices in a weighted graph. It uses a greedy approach to repeatedly select the nearest unvisited vertex and efficiently calculate shortest paths.
"""