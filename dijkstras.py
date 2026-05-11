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

    for i in range(v):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            u = i

    visited[u] = True

    for j in range(v):
        if graph[u][j] > 0 and not visited[j]:
            if distance[u] + graph[u][j] < distance[j]:
                distance[j] = distance[u] + graph[u][j]

print("\nVertex\tDistance")

for i in range(v):
    print(i, "\t", distance[i])


"""Title
Dijkstra’s Shortest Path Algorithm in Python
Objective
To find the shortest distance from a source vertex to all other vertices in a weighted graph using Dijkstra’s Algorithm.

Theory
Dijkstra’s Algorithm is a graph search algorithm used to find the shortest path from one source vertex to all other vertices in a weighted graph. It works only for graphs with non-negative edge weights. The algorithm starts from a selected source vertex and repeatedly chooses the unvisited vertex with the minimum distance. Then it updates the distances of its neighboring vertices if a shorter path is found.
In this program, the graph is represented using an adjacency matrix. Each value in the matrix represents the weight or cost between two vertices. If the value is 0, it means there is no direct connection between those vertices.
The program uses two important arrays:

visited[] → stores whether a vertex has been processed.
distance[] → stores the shortest distance from the source vertex.

Initially, all distances are set to infinity (inf) because shortest paths are not known. The source vertex distance is set to 0 because the distance from the source to itself is zero.
The algorithm repeatedly selects the vertex having the minimum distance among unvisited vertices. After selecting a vertex, it checks all adjacent vertices and updates their distances if a shorter path is found. This process continues until all vertices are visited.
Important Points

Dijkstra’s Algorithm
Finds shortest path from source vertex.
Works on weighted graphs.

Weighted Graph
Each edge has a cost or weight.

Adjacency Matrix

Graph is stored in matrix form.
0 means no edge exists.

Distance Array
Stores shortest distance from source.

Visited Array
Keeps track of processed vertices.

Infinity Value
float('inf') represents unknown large distance.

Minimum Distance Vertex
Algorithm selects the smallest unvisited distance.

Distance Update

If a shorter path is found:
distance[u] + graph[u][j] < distance[j]
Update the distance.


Greedy Algorithm
Chooses locally smallest distance each time.


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
Mark it visited.
Check all adjacent vertices.
Update distance if shorter path exists.
Print shortest distances.
End the program.


Conclusion
This program implements Dijkstra’s Algorithm to find the shortest path from a source vertex to all other vertices in a weighted graph. It uses a greedy approach to repeatedly choose the nearest unvisited vertex and update distances efficiently. The algorithm is widely used in real-world navigation and routing systems."""